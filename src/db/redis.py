import redis.asyncio as redis
from src.config import Config

# Create Redis connection
redis_token_blocklist = redis.Redis(
    host=Config.REDIS_HOST,
    port=Config.REDIS_PORT,
    db=0,
    decode_responses=True   # ensures string values instead of bytes
)

# Add a token JTI to blocklist
async def add_jti_to_blocklist(jti: str) -> None:
    await redis_token_blocklist.set(
        name=jti,
        value="",   # store empty string (just need presence)
        ex=3600     # expiration time = 1 hour
    )

# Check if a token JTI is in the blocklist
async def token_in_blocklist(jti: str) -> bool:
    value = await redis_token_blocklist.get(jti)
    return value is not None
