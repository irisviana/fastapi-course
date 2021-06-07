from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session


from schemas.users import UserCreate, Show_user
from db.session import get_db
from db.repository.users import create_new_user


router = APIRouter()


@router.post("/", response_model=Show_user)  # limit user atributs
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    user = create_new_user(user, db)
    return user
