import re
from datetime import datetime


class PDFParser:

    @staticmethod
    def extract_notification_no(text):

        match = re.search(
            r"NOTIFICATION\s*NO\.?\s*([0-9/]+)",
            text,
            re.IGNORECASE,
        )

        if match:
            return match.group(1)

        return None

    @staticmethod
    def extract_vacancies(text):

        match = re.search(
            r"for\s+(\d+)\s+vacancies",
            text,
            re.IGNORECASE,
        )

        if match:
            return int(match.group(1))

        return None

    @staticmethod
    def extract_salary(text):

        match = re.search(
            r"Rs\.?\s*([\d,]+)\s*[–-]\s*([\d,]+)",
            text,
            re.IGNORECASE,
        )

        if match:
            return (
                f"Rs.{match.group(1)} - Rs.{match.group(2)}"
            )

        return None

    @staticmethod
    def extract_age_limit(text):

        match = re.search(
            r"maximum age of\s+(\d+)\s+years",
            text,
            re.IGNORECASE,
        )

        if match:
            return match.group(1) + " Years"

        return None

    @staticmethod
    def extract_application_dates(text):

        match = re.search(
            r"from\s+(\d{2}/\d{2}/\d{4})\s+to\s+(\d{2}/\d{2}/\d{4})",
            text,
            re.IGNORECASE,
        )

        if not match:
            return None, None

        start = datetime.strptime(
            match.group(1),
            "%d/%m/%Y"
        ).date()

        end = datetime.strptime(
            match.group(2),
            "%d/%m/%Y"
        ).date()

        return start, end