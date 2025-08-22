from fastapi import status, HTTPException, APIRouter, Depends
from .schemas import Book, BookUpdateModel, BookCreateModel
from src.db.main import get_session
from sqlmodel.ext.asyncio.session import AsyncSession
from .service import BookService
from src.books.models import Book
from src.auth.dependencies import AccessTokenBearer


book_router = APIRouter()
book_service = BookService()
access_token_bearer = AccessTokenBearer()


@book_router.get("/", response_model=list[Book])
async def get_all_books(session: AsyncSession = Depends(get_session), user_details=Depends(access_token_bearer)):
    print(user_details)
    books = await book_service.get_all_books(session)
    return books

@book_router.post("/", status_code=status.HTTP_201_CREATED, response_model=Book)
async def create_a_book(book_data:BookCreateModel, session: AsyncSession = Depends(get_session), user_details=Depends(access_token_bearer)) -> dict:
    new_book = await book_service.create_a_book(book_data, session)
    return new_book

@book_router.get("/{book_uid}", response_model=Book)
async def get_a_book(book_uid: str, session: AsyncSession = Depends(get_session), user_details=Depends(access_token_bearer)) -> dict:
    book = await book_service.get_book(book_uid, session)
    if book:
        return book
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"error": "Book not Found!"})

@book_router.patch("/{book_uid}", response_model=Book)
async def update_book(book_uid: str, bookUpdateData: BookUpdateModel, session: AsyncSession = Depends(get_session), user_details=Depends(access_token_bearer)):
    book_update = await book_service.update_book(book_uid, bookUpdateData, session)
    if book_update:
        return book_update
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"error": "Book not Found!"})

@book_router.delete("/{book_uid}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_uid: str, session: AsyncSession = Depends(get_session), user_details=Depends(access_token_bearer)):
    book_delete = book_service.delete_book(book_uid, session)
    if book_delete:
        return {"message": "Book {book_uid} is Deleted"}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"error": "Book not Found!"}) 