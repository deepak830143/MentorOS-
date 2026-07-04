from typing import List, Optional

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.db.session import get_db

from app.schemas.exam_notification import (
    ExamNotificationCreate,
    ExamNotificationResponse,
)

from app.services.exam_notification_service import (
    ExamNotificationService,
)

router = APIRouter(
    prefix="/api/v1/notifications",
    tags=["Notifications"],
)


# ==========================================================
# CREATE
# ==========================================================

@router.post(
    "",
    response_model=ExamNotificationResponse,
)
def create_notification(
    notification: ExamNotificationCreate,
    db: Session = Depends(get_db),
):
    return ExamNotificationService.create_notification(
        db,
        notification,
    )


# ==========================================================
# SEARCH + FILTER + PAGINATION + SORTING
# ==========================================================

@router.get(
    "",
    response_model=List[ExamNotificationResponse],
)
def search_notifications(

    source: Optional[str] = Query(None),

    organization: Optional[str] = Query(None),

    exam_name: Optional[str] = Query(None),

    notification_no: Optional[str] = Query(None),

    category: Optional[str] = Query(None),

    qualification: Optional[str] = Query(None),

    status: Optional[str] = Query(None),

    page: int = Query(
        1,
        ge=1,
    ),

    size: int = Query(
        20,
        ge=1,
        le=100,
    ),

    sort_by: str = Query(
        "created_at",
    ),

    sort_order: str = Query(
        "desc",
    ),

    db: Session = Depends(get_db),

):

    return ExamNotificationService.search_notifications(

        db=db,

        source=source,

        organization=organization,

        exam_name=exam_name,

        notification_no=notification_no,

        category=category,

        qualification=qualification,

        status=status,

        page=page,

        size=size,

        sort_by=sort_by,

        sort_order=sort_order,
    )


# ==========================================================
# GET BY ID
# ==========================================================

@router.get(
    "/{notification_id}",
    response_model=ExamNotificationResponse,
)
def get_notification(
    notification_id: int,
    db: Session = Depends(get_db),
):

    return ExamNotificationService.get_notification(
        db,
        notification_id,
    )


# ==========================================================
# DELETE
# ==========================================================

@router.delete(
    "/{notification_id}",
)
def delete_notification(
    notification_id: int,
    db: Session = Depends(get_db),
):

    return ExamNotificationService.delete_notification(
        db,
        notification_id,
    )