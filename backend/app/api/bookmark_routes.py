from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.security import get_current_user

from app.db.session import get_db

from app.models.user import User

from app.schemas.bookmark import (
    BookmarkResponse,
    SavedNotificationResponse,
)

from app.services.bookmark_service import (
    BookmarkService,
)

router = APIRouter(
    prefix="/api/v1/bookmarks",
    tags=["Bookmarks"],
)

# ==========================================================
# ADD BOOKMARK
# ==========================================================

@router.post(
    "/{notification_id}",
    response_model=BookmarkResponse,
)
def add_bookmark(

    notification_id: int,

    current_user: User = Depends(
        get_current_user
    ),

    db: Session = Depends(get_db),

):

    return BookmarkService.add_bookmark(

        db=db,

        user_id=current_user.id,

        notification_id=notification_id,
    )


# ==========================================================
# GET USER BOOKMARKS
# ==========================================================

@router.get(
    "",
    response_model=List[
        SavedNotificationResponse
    ],
)
def get_bookmarks(

    current_user: User = Depends(
        get_current_user
    ),

    db: Session = Depends(get_db),

):

    return BookmarkService.get_user_bookmarks(

        db=db,

        user_id=current_user.id,
    )


# ==========================================================
# COUNT BOOKMARKS
# ==========================================================

@router.get(
    "/count",
)
def count_bookmarks(

    current_user: User = Depends(
        get_current_user
    ),

    db: Session = Depends(get_db),

):

    return BookmarkService.count_bookmarks(

        db=db,

        user_id=current_user.id,
    )


# ==========================================================
# DELETE BOOKMARK
# ==========================================================

@router.delete(
    "/{notification_id}",
)
def delete_bookmark(

    notification_id: int,

    current_user: User = Depends(
        get_current_user
    ),

    db: Session = Depends(get_db),

):

    return BookmarkService.remove_bookmark(

        db=db,

        user_id=current_user.id,

        notification_id=notification_id,
    )