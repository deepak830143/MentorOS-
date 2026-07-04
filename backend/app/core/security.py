from datetime import datetime, timedelta

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session

from app.core.config import settings
from app.db.session import get_db
from app.models.user import User
from app.repositories.user_repository import UserRepository

# ==========================================================
# JWT CONFIGURATION
# ==========================================================

SECRET_KEY = settings.SECRET_KEY

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/v1/auth/login"
)


# ==========================================================
# CREATE ACCESS TOKEN
# ==========================================================

def create_access_token(data: dict):

    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM,
    )

    return encoded_jwt


# ==========================================================
# VERIFY ACCESS TOKEN
# ==========================================================

def verify_access_token(token: str):

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM],
        )

        return payload

    except JWTError:

        return None


# ==========================================================
# GET CURRENT USER
# ==========================================================

def get_current_user(

    token: str = Depends(oauth2_scheme),

    db: Session = Depends(get_db),

):

    payload = verify_access_token(token)

    if payload is None:

        raise HTTPException(

            status_code=status.HTTP_401_UNAUTHORIZED,

            detail="Invalid authentication credentials",

        )

    email = payload.get("sub")

    if email is None:

        raise HTTPException(

            status_code=status.HTTP_401_UNAUTHORIZED,

            detail="Invalid authentication credentials",

        )

    user = UserRepository.get_by_email(
        db,
        email,
    )

    if user is None:

        raise HTTPException(

            status_code=status.HTTP_401_UNAUTHORIZED,

            detail="User not found",

        )

    return user