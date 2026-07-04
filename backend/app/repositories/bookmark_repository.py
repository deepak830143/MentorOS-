from sqlalchemy.orm import Session

from app.models.bookmark import Bookmark
from app.models.exam_notification import ExamNotification


class BookmarkRepository:

    # ==========================================================
    # CREATE BOOKMARK
    # ==========================================================

    @staticmethod
    def create(
        db: Session,
        user_id: int,
        notification_id: int,
    ):

        bookmark = Bookmark(
            user_id=user_id,
            notification_id=notification_id,
        )

        db.add(bookmark)
        db.commit()
        db.refresh(bookmark)

        return bookmark

    # ==========================================================
    # GET BY USER & NOTIFICATION
    # ==========================================================

    @staticmethod
    def get_by_user_notification(
        db: Session,
        user_id: int,
        notification_id: int,
    ):

        return (
            db.query(Bookmark)
            .filter(
                Bookmark.user_id == user_id,
                Bookmark.notification_id == notification_id,
            )
            .first()
        )

    # ==========================================================
    # GET USER BOOKMARKS
    # ==========================================================

    @staticmethod
    def get_user_bookmarks(
        db: Session,
        user_id: int,
    ):

        return (
            db.query(
                Bookmark,
                ExamNotification,
            )
            .join(
                ExamNotification,
                Bookmark.notification_id == ExamNotification.id,
            )
            .filter(
                Bookmark.user_id == user_id
            )
            .order_by(
                Bookmark.created_at.desc()
            )
            .all()
        )

    # ==========================================================
    # DELETE BOOKMARK
    # ==========================================================

    @staticmethod
    def delete(
        db: Session,
        bookmark: Bookmark,
    ):

        db.delete(bookmark)
        db.commit()

    # ==========================================================
    # DELETE BY USER & NOTIFICATION
    # ==========================================================

    @staticmethod
    def delete_by_user_notification(
        db: Session,
        user_id: int,
        notification_id: int,
    ):

        bookmark = (
            db.query(Bookmark)
            .filter(
                Bookmark.user_id == user_id,
                Bookmark.notification_id == notification_id,
            )
            .first()
        )

        if bookmark:

            db.delete(bookmark)
            db.commit()

        return bookmark

    # ==========================================================
    # COUNT USER BOOKMARKS
    # ==========================================================

    @staticmethod
    def count(
        db: Session,
        user_id: int,
    ):

        return (
            db.query(Bookmark)
            .filter(
                Bookmark.user_id == user_id
            )
            .count()
        )