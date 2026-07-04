import requests
from sqlalchemy.orm import Session

from app.collectors.common.base_collector import BaseCollector
from app.collectors.appsc.parser import APPSCParser
from app.collectors.appsc.config import (
    NOTIFICATION_PAGE,
    REQUEST_TIMEOUT,
    HEADERS,
)

from app.db.database import SessionLocal

from app.schemas.exam_notification import ExamNotificationCreate
from app.services.exam_notification_service import ExamNotificationService
from app.services.pdf_processing_service import PDFProcessingService
from app.services.ai_summary_service import AISummaryService


class APPSCCollector(BaseCollector):
    """
    APPSC Recruitment Notification Collector
    """

    def __init__(self):

        self.parser = APPSCParser()
        self.pdf_service = PDFProcessingService()

    # -------------------------------------------------
    # FETCH
    # -------------------------------------------------

    def fetch(self):

        print("🌐 Connecting to APPSC...")
        print(f"URL : {NOTIFICATION_PAGE}")

        try:

            response = requests.get(
                NOTIFICATION_PAGE,
                headers=HEADERS,
                timeout=REQUEST_TIMEOUT,
                allow_redirects=True,
            )

            print(f"Status Code : {response.status_code}")
            print(f"Final URL   : {response.url}")

            response.raise_for_status()

            html = response.text

            with open(
                "appsc_page.html",
                "w",
                encoding="utf-8",
            ) as file:
                file.write(html)

            print("✅ HTML saved as appsc_page.html")

            return html

        except requests.exceptions.RequestException as e:

            print(f"❌ Failed to connect : {e}")

            return ""

    # -------------------------------------------------
    # PARSE
    # -------------------------------------------------

    def parse(self, raw_data):

        if not raw_data:
            return []

        return self.parser.parse(raw_data)

    # -------------------------------------------------
    # VALIDATE
    # -------------------------------------------------

    def validate(self, notifications):

        valid = []

        for item in notifications:

            if item.get("title"):
                valid.append(item)

        print(f"✅ Valid Notifications : {len(valid)}")

        return valid

    # -------------------------------------------------
    # SAVE
    # -------------------------------------------------

    def save(self, notifications):

        db: Session = SessionLocal()

        saved = 0
        skipped = 0

        try:

            for item in notifications:

                print("\n" + "-" * 80)
                print(item["title"])

                # -------------------------------------------------
                # Process PDF
                # -------------------------------------------------

                pdf_data = self.pdf_service.process(
                    item["pdf_url"]
                )

                print("\nPDF DATA")
                print(pdf_data)

                # -------------------------------------------------
                # Generate AI Summary
                # -------------------------------------------------

                ai_summary = AISummaryService.generate(
                    {
                        "organization": "Andhra Pradesh Public Service Commission",
                        "notification_no": pdf_data.get("notification_no"),
                        "exam_name": pdf_data.get("post_name")
                        or item["title"],
                        "vacancies": pdf_data.get("vacancies"),
                        "salary": pdf_data.get("salary"),
                        "age_limit": pdf_data.get("age_limit"),
                        "qualification": pdf_data.get("qualification"),
                        "application_start": pdf_data.get(
                            "application_start"
                        ),
                        "application_end": pdf_data.get(
                            "application_end"
                        ),
                    }
                )

                print("\n" + "=" * 80)
                print("AI SUMMARY")
                print("=" * 80)
                print(ai_summary)
                print("=" * 80)

                # -------------------------------------------------
                # Build Notification Object
                # -------------------------------------------------

                notification = ExamNotificationCreate(

                    source="APPSC",

                    organization="Andhra Pradesh Public Service Commission",

                    exam_name=pdf_data.get("post_name")
                    or item["title"],

                    notification_no=pdf_data.get(
                        "notification_no"
                    ),

                    title=item["title"],

                    category=item.get(
                        "recruitment_type"
                    )
                    or "Recruitment",

                    status="OPEN",

                    vacancies=pdf_data.get(
                        "vacancies"
                    ),

                    qualification=pdf_data.get(
                        "qualification"
                    ),

                    age_limit=pdf_data.get(
                        "age_limit"
                    ),

                    salary=pdf_data.get(
                        "salary"
                    ),

                    application_start=pdf_data.get(
                        "application_start"
                    ),

                    application_end=pdf_data.get(
                        "application_end"
                    ),

                    pdf_url=item["pdf_url"],

                    official_url=NOTIFICATION_PAGE,

                    ai_summary=ai_summary,
                )

                print("\nNOTIFICATION OBJECT")
                print(notification.model_dump())

                # -------------------------------------------------
                # Save Notification
                # -------------------------------------------------

                try:

                    saved_notification = (
                        ExamNotificationService.create_notification(
                            db,
                            notification,
                        )
                    )

                    print("\nSAVED DATABASE OBJECT")
                    print(saved_notification.ai_summary)

                    saved += 1

                    print("✅ Saved")

                except Exception as e:

                    skipped += 1

                    print("❌ Failed")
                    print(e)

            print("\n" + "=" * 80)
            print("APPSC SUMMARY")
            print("=" * 80)

            print(f"Total Notifications : {len(notifications)}")
            print(f"Saved               : {saved}")
            print(f"Skipped             : {skipped}")

            print("=" * 80)

        finally:

            db.close()