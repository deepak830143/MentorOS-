from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.exam_notification import ExamNotification


class DashboardRepository:

    # ---------------------------------------------------------
    # Dashboard Statistics
    # ---------------------------------------------------------

    @staticmethod
    def get_dashboard(db: Session):

        total_notifications = (
            db.query(ExamNotification)
            .count()
        )

        open_notifications = (
            db.query(ExamNotification)
            .filter(
                ExamNotification.status == "OPEN"
            )
            .count()
        )

        closed_notifications = (
            db.query(ExamNotification)
            .filter(
                ExamNotification.status == "CLOSED"
            )
            .count()
        )

        organizations = (
            db.query(
                ExamNotification.organization
            )
            .distinct()
            .count()
        )

        # ---------------------------------------------------------
        # Latest Notifications
        # ---------------------------------------------------------

        latest_notifications = (
            db.query(ExamNotification)
            .order_by(
                ExamNotification.created_at.desc()
            )
            .limit(10)
            .all()
        )

        # ---------------------------------------------------------
        # Category Distribution
        # ---------------------------------------------------------

        category_result = (
            db.query(
                ExamNotification.category,
                func.count(ExamNotification.id)
            )
            .group_by(
                ExamNotification.category
            )
            .all()
        )

        category_distribution = {
            category: count
            for category, count in category_result
        }

        # ---------------------------------------------------------
        # Organization Distribution
        # ---------------------------------------------------------

        organization_result = (
            db.query(
                ExamNotification.organization,
                func.count(ExamNotification.id)
            )
            .group_by(
                ExamNotification.organization
            )
            .all()
        )

        organization_distribution = {
            organization: count
            for organization, count in organization_result
        }

        return {

            "total_notifications": total_notifications,

            "open_notifications": open_notifications,

            "closed_notifications": closed_notifications,

            "organizations": organizations,

            "latest_notifications": latest_notifications,

            "category_distribution": category_distribution,

            "organization_distribution": organization_distribution,
        }