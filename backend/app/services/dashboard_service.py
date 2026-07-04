from sqlalchemy.orm import Session

from app.repositories.dashboard_repository import (
    DashboardRepository,
)


class DashboardService:

    # ---------------------------------------------------------
    # GET DASHBOARD
    # ---------------------------------------------------------

    @staticmethod
    def get_dashboard(
        db: Session,
    ):

        data = DashboardRepository.get_dashboard(
            db,
        )

        latest_notifications = []

        for notification in data["latest_notifications"]:

            latest_notifications.append(
                {
                    "id": notification.id,
                    "exam_name": notification.exam_name,
                    "notification_no": notification.notification_no,
                    "organization": notification.organization,
                    "application_end": (
                        str(notification.application_end)
                        if notification.application_end
                        else None
                    ),
                }
            )

        return {

            "total_notifications":
                data["total_notifications"],

            "open_notifications":
                data["open_notifications"],

            "closed_notifications":
                data["closed_notifications"],

            "organizations":
                data["organizations"],

            "latest_notifications":
                latest_notifications,

            "category_distribution":
                data["category_distribution"],

            "organization_distribution":
                data["organization_distribution"],
        }