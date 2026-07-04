import re
from datetime import datetime

from app.extraction.extractor import FieldExtractor
from app.extraction.qualification_extractor import QualificationExtractor


class PDFParser:
    """
    Extract structured information from Government Recruitment PDFs.
    """

    def parse(self, text: str):

        data = {}

        # --------------------------------------------------
        # Notification Number
        # --------------------------------------------------
        match = re.search(
            r"NOTIFICATION\s+NO\.?\s*([0-9]+/[0-9]+)",
            text,
            re.IGNORECASE,
        )

        data["notification_no"] = (
            match.group(1)
            if match
            else None
        )

        # --------------------------------------------------
        # Notification Date
        # --------------------------------------------------
        match = re.search(
            r"DATED[:\s]*([0-9]{2}\.[0-9]{2}\.[0-9]{4})",
            text,
            re.IGNORECASE,
        )

        data["notification_date"] = (
            match.group(1)
            if match
            else None
        )

        # --------------------------------------------------
        # Post Name
        # --------------------------------------------------
        match = re.search(
            r"POST OF\s+(.*?)\s+IN",
            text,
            re.IGNORECASE,
        )

        data["post_name"] = (
            match.group(1).title().strip()
            if match
            else None
        )

        # --------------------------------------------------
        # Department
        # --------------------------------------------------
        match = re.search(
            r"IN\s+(.*?)\n",
            text,
            re.IGNORECASE,
        )

        data["department"] = (
            match.group(1).strip()
            if match
            else None
        )

        # --------------------------------------------------
        # Vacancies
        # --------------------------------------------------
        data["vacancies"] = (
            FieldExtractor.extract_vacancies(text)
        )

        # --------------------------------------------------
        # Salary
        # --------------------------------------------------
        data["salary"] = (
            FieldExtractor.extract_salary(text)
        )

        # --------------------------------------------------
        # Age Limit
        # --------------------------------------------------
        data["age_limit"] = (
            FieldExtractor.extract_age(text)
        )

        # --------------------------------------------------
        # Application Dates
        # --------------------------------------------------
        dates = re.findall(
            r"([0-9]{2}/[0-9]{2}/[0-9]{4})",
            text,
        )

        if len(dates) >= 2:

            data["application_start"] = datetime.strptime(
                dates[0],
                "%d/%m/%Y",
            ).date()

            data["application_end"] = datetime.strptime(
                dates[1],
                "%d/%m/%Y",
            ).date()

        else:

            data["application_start"] = None
            data["application_end"] = None

        # --------------------------------------------------
        # Qualification
        # --------------------------------------------------
        data["qualification"] = (
            QualificationExtractor.extract(text)
        )

        return data