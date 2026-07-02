from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate
from app.utils.security import verify_password
from app.core.security import create_access_token


class AuthService:

    @staticmethod
    def register_user(db: Session, user: UserCreate):

        existing_user = UserRepository.get_by_email(
            db,
            user.email
        )

        if existing_user:
            raise HTTPException(
                status_code=400,
                detail="Email already registered"
            )

        return UserRepository.create(db, user)

    @staticmethod
    def login_user(db: Session, email: str, password: str):

        user = UserRepository.authenticate(db, email)

        if not user:
            raise HTTPException(
                status_code=401,
                detail="Invalid email or password"
            )

        if not verify_password(password, user.password):
            raise HTTPException(
                status_code=401,
                detail="Invalid email or password"
            )

        access_token = create_access_token(
            data={"sub": user.email}
        )

        return {
            "access_token": access_token,
            "token_type": "bearer"
        }