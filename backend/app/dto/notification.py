from dataclasses import dataclass
from typing import Optional


@dataclass
class NotificationDTO:
    source: str
    organization: str
    exam_name: str
    title: str

    notification_no: Optional[str] = None
    category: Optional[str] = None

    pdf_url: Optional[str] = None
    apply_url: Optional[str] = None
    official_url: Optional[str] = None

    vacancies: Optional[int] = None

    qualification: Optional[str] = None

    age_limit: Optional[str] = None

    salary: Optional[str] = None

    description: Optional[str] = None