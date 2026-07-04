from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.exam_notification import ExamNotification
from app.repositories.bookmark_repository import (
    BookmarkRepository,
)


class BookmarkService:

    # ==========================================================
    # ADD BOOKMARK
    # ==========================================================

    @staticmethod
    def add_bookmark(
        db: Session,
        user_id: int,
        notification_id: int,
    ):

        notification = (
            db.query(ExamNotification)
            .filter(
                ExamNotification.id == notification_id
            )
            .first()
        )

        if notification is None:

            raise HTTPException(
                status_code=404,
                detail="Notification not found",
            )

        existing = (
            BookmarkRepository.get_by_user_notification(
                db,
                user_id,
                notification_id,
            )
        )

        if existing:

            raise HTTPException(
                status_code=400,
                detail="Notification already bookmarked",
            )

        return BookmarkRepository.create(
            db,
            user_id,
            notification_id,
        )

    # ==========================================================
    # GET USER BOOKMARKS
    # ==========================================================

    @staticmethod
    def get_user_bookmarks(
        db: Session,
        user_id: int,
    ):

        rows = BookmarkRepository.get_user_bookmarks(
            db,
            user_id,
        )

        results = []

        for _, notification in rows:

            results.append(
                {
                    "id": notification.id,
                    "exam_name": notification.exam_name,
                    "notification_no": notification.notification_no,
                    "organization": notification.organization,
                    "category": notification.category,
                    "vacancies": notification.vacancies,
                    "application_end": (
                        str(notification.application_end)
                        if notification.application_end
                        else None
                    ),
                    "pdf_url": notification.pdf_url,
                    "ai_summary": notification.ai_summary,
                }
            )

        return results

    # ==========================================================
    # REMOVE BOOKMARK
    # ==========================================================

    @staticmethod
    def remove_bookmark(
        db: Session,
        user_id: int,
        notification_id: int,
    ):

        bookmark = (
            BookmarkRepository.delete_by_user_notification(
                db,
                user_id,
                notification_id,
            )
        )

        if bookmark is None:

            raise HTTPException(
                status_code=404,
                detail="Bookmark not found",
            )

        return {
            "message": "Bookmark removed successfully"
        }

    # ==========================================================
    # COUNT BOOKMARKS
    # ==========================================================

    @staticmethod
    def count_bookmarks(
        db: Session,
        user_id: int,
    ):

        return {
            "count": BookmarkRepository.count(
                db,
                user_id,
            )
        }