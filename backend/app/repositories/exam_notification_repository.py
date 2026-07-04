from sqlalchemy import asc, desc
from sqlalchemy.orm import Session

from app.models.exam_notification import ExamNotification
from app.schemas.exam_notification import ExamNotificationCreate


class ExamNotificationRepository:

    # ---------------------------------------------------------
    # CREATE
    # ---------------------------------------------------------

    @staticmethod
    def create(
        db: Session,
        notification: ExamNotificationCreate,
    ):

        db_notification = ExamNotification(
            **notification.model_dump()
        )

        db.add(db_notification)
        db.commit()
        db.refresh(db_notification)

        return db_notification

    # ---------------------------------------------------------
    # GET ALL
    # ---------------------------------------------------------

    @staticmethod
    def get_all(db: Session):

        return (
            db.query(ExamNotification)
            .order_by(
                ExamNotification.created_at.desc()
            )
            .all()
        )

    # ---------------------------------------------------------
    # SEARCH + FILTER + PAGINATION
    # ---------------------------------------------------------

    @staticmethod
    def search(
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

        query = db.query(
            ExamNotification
        )

        # ------------------------------------
        # Filters
        # ------------------------------------

        if source:

            query = query.filter(
                ExamNotification.source.ilike(
                    f"%{source}%"
                )
            )

        if organization:

            query = query.filter(
                ExamNotification.organization.ilike(
                    f"%{organization}%"
                )
            )

        if exam_name:

            query = query.filter(
                ExamNotification.exam_name.ilike(
                    f"%{exam_name}%"
                )
            )

        if notification_no:

            query = query.filter(
                ExamNotification.notification_no.ilike(
                    f"%{notification_no}%"
                )
            )

        if category:

            query = query.filter(
                ExamNotification.category.ilike(
                    f"%{category}%"
                )
            )

        if qualification:

            query = query.filter(
                ExamNotification.qualification.ilike(
                    f"%{qualification}%"
                )
            )

        if status:

            query = query.filter(
                ExamNotification.status == status
            )

        # ------------------------------------
        # Sorting
        # ------------------------------------

        if hasattr(
            ExamNotification,
            sort_by,
        ):

            column = getattr(
                ExamNotification,
                sort_by,
            )

            if sort_order.lower() == "asc":

                query = query.order_by(
                    asc(column)
                )

            else:

                query = query.order_by(
                    desc(column)
                )

        else:

            query = query.order_by(
                ExamNotification.created_at.desc()
            )

        # ------------------------------------
        # Pagination
        # ------------------------------------

        offset = (
            page - 1
        ) * size

        query = (
            query
            .offset(offset)
            .limit(size)
        )

        return query.all()

    # ---------------------------------------------------------
    # GET BY ID
    # ---------------------------------------------------------

    @staticmethod
    def get_by_id(
        db: Session,
        notification_id: int,
    ):

        return (
            db.query(
                ExamNotification
            )
            .filter(
                ExamNotification.id ==
                notification_id
            )
            .first()
        )

    # ---------------------------------------------------------
    # GET BY HASH
    # ---------------------------------------------------------

    @staticmethod
    def get_by_hash(
        db: Session,
        notification_hash: str,
    ):

        return (
            db.query(
                ExamNotification
            )
            .filter(
                ExamNotification.notification_hash ==
                notification_hash
            )
            .first()
        )

    # ---------------------------------------------------------
    # DELETE
    # ---------------------------------------------------------

    @staticmethod
    def delete(
        db: Session,
        notification_id: int,
    ):

        notification = (
            db.query(
                ExamNotification
            )
            .filter(
                ExamNotification.id ==
                notification_id
            )
            .first()
        )

        if notification:

            db.delete(notification)
            db.commit()

        return notification