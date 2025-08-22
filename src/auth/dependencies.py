'''
HTTPBearer
It is a security scheme that tells FastAPI how to extract a Bearer token from the Authorization header of incoming requests.

HTTPAuthorizationCredentials
It’s a Pydantic model-like object that holds the extracted info from the Authorization header.
It has two attributes:
scheme → usually "Bearer", the auth scheme.
credentials → the actual token (e.g., your JWT string).

'''
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Request, HTTPException, status
from .utils import decode_token
from src.db.redis import token_in_blocklist

class TokenBearer(HTTPBearer):
    
    def __init__(self, auto_error=True):
        super().__init__(auto_error=auto_error)

    async def __call__(self, request: Request) -> HTTPAuthorizationCredentials | None:
        creds = await super().__call__(request)
        token = creds.credentials
        token_data = decode_token(token)

        if not self.token_valid(token):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Invalid or Expired Token"
            )
        if await token_in_blocklist(token_data["jti"]):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail={
                    "error": "This token is invalid or has be revoked",
                    "resolution": "Please get a new token"
                }
            )
        
        self.verify_token_data(token_data)

        return token_data
    
    def token_valid(self, token:str) -> bool:
        token_data = decode_token(token)
        return True if token_data is not None else False
    
    def verify_token_data(self, token_data):
        raise NotImplementedError("Please Overide this method in child class")
        
class AccessTokenBearer(TokenBearer):
    
    def verify_token_data(self, token_data: dict) -> None:
        if token_data and token_data["refresh"]:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Please provide an Access Token"
            ) 


class RefreshTokenBearer(TokenBearer):
    def verify_token_data(self, token_data: dict) -> None:
        if token_data and not token_data["refresh"]:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Please provide an Refresh Token"
            ) 