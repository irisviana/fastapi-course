from typing import Optional
from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


class Show_user(BaseModel):
    username: str
    email: EmailStr
    is_activate: bool


    class Config():
    	orm_mode = True 

