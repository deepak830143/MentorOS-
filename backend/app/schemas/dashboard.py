from typing import List

from pydantic import BaseModel


class LatestNotification(BaseModel):
    id: int
    exam_name: str
    notification_no: str | None = None
    organization: str
    application_end: str | None = None


class DashboardResponse(BaseModel):
    total_notifications: int
    open_notifications: int
    closed_notifications: int
    organizations: int

    latest_notifications: List[LatestNotification]

    category_distribution: dict[str, int]
    organization_distribution: dict[str, int]