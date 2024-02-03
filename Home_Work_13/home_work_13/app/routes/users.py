from fastapi import APIRouter, Depends
from app.database.db import get_db, SessionLocal
from app.database.auth import create_access_token, DefaultUser
from app.schemas.user import User
from app.services.users import UserService
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter()


@router.post("/register/", response_model=User)
async def register(user: User, db: SessionLocal = Depends(get_db)):
    user_service = UserService(db)
    return user_service.create_new(user)


@router.get("/protected-resource/", response_model=User)
async def protected_resource(current_user: DefaultUser):
    return current_user
