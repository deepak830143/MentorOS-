from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.repositories.exam_notification_repository import (
    ExamNotificationRepository,
)

from app.schemas.exam_notification import (
    ExamNotificationCreate,
)

from app.utils.notification_hash import (
    generate_notification_hash,
)


class ExamNotificationService:

    # ---------------------------------------------------------
    # CREATE
    # ---------------------------------------------------------

    @staticmethod
    def create_notification(
        db: Session,
        notification: ExamNotificationCreate,
    ):

        notification_hash = generate_notification_hash(
            source=notification.source,
            organization=notification.organization,
            exam_name=notification.exam_name,
            notification_no=notification.notification_no,
            title=notification.title,
        )

        existing = ExamNotificationRepository.get_by_hash(
            db,
            notification_hash,
        )

        if existing:
            return existing

        data = notification.model_dump()

        data["notification_hash"] = notification_hash

        db_notification = ExamNotificationCreate(
            **data
        )

        return ExamNotificationRepository.create(
            db,
            db_notification,
        )

    # ---------------------------------------------------------
    # SEARCH
    # ---------------------------------------------------------

    @staticmethod
    def search_notifications(

        db: Session,

        source: str | None = None,
        organization: str | None = None,
        exam_name: str | None = None,
        notification_no: str | None = None,
        category: str | None = None,
        qualification: str | None = None,
        status: str | None = None,

        page: int = 1,
        size: int = 20,

        sort_by: str = "created_at",
        sort_order: str = "desc",

    ):

        return ExamNotificationRepository.search(

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

    # ---------------------------------------------------------
    # GET ALL
    # ---------------------------------------------------------

    @staticmethod
    def get_all_notifications(
        db: Session,
    ):

        return ExamNotificationRepository.get_all(
            db
        )

    # ---------------------------------------------------------
    # GET ONE
    # ---------------------------------------------------------

    @staticmethod
    def get_notification(
        db: Session,
        notification_id: int,
    ):

        notification = (
            ExamNotificationRepository.get_by_id(
                db,
                notification_id,
            )
        )

        if notification is None:

            raise HTTPException(

                status_code=404,

                detail="Notification not found",

            )

        return notification

    # ---------------------------------------------------------
    # DELETE
    # ---------------------------------------------------------

    @staticmethod
    def delete_notification(
        db: Session,
        notification_id: int,
    ):

        notification = (
            ExamNotificationRepository.delete(
                db,
                notification_id,
            )
        )

        if notification is None:

            raise HTTPException(

                status_code=404,

                detail="Notification not found",

            )

        return {
            "message": "Notification deleted successfully"
        }