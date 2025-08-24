from pydantic import BaseModel, Field
import uuid
from datetime import datetime
from typing import List
from src.books.schemas import Book
from src.reviews.schemas import ReviewModel


class UserCreateModel(BaseModel):
    username: str = Field(max_length=10)
    email: str = Field(max_length=40)
    password: str = Field(max_length=10)
    first_name: str
    last_name: str

class UserModel(BaseModel):
    uid: uuid.UUID
    username: str
    email: str
    first_name: str
    last_name: str
    is_verified: bool
    password_hash: str = Field(exclude=True)
    created_at: datetime 
    update_at: datetime 

class UserBookModel(UserModel):
    books: List[Book]
    reviews: List[ReviewModel]

class UserLoginModel(BaseModel):
    email: str = Field(max_length=40)
    password: str = Field(max_length=10)