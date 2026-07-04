import re

from app.extraction.patterns import (
    SALARY_PATTERNS,
    VACANCY_PATTERNS,
    AGE_PATTERNS,
)


class FieldExtractor:

    @staticmethod
    def extract_salary(text):

        for pattern in SALARY_PATTERNS:

            match = re.search(
                pattern,
                text,
                re.IGNORECASE,
            )

            if match:

                return (
                    f"Rs.{match.group(1)} - Rs.{match.group(2)}"
                )

        return None

    @staticmethod
    def extract_vacancies(text):

        for pattern in VACANCY_PATTERNS:

            match = re.search(
                pattern,
                text,
                re.IGNORECASE,
            )

            if match:

                return int(match.group(1))

        return None

    @staticmethod
    def extract_age(text):

        for pattern in AGE_PATTERNS:

            match = re.search(
                pattern,
                text,
                re.IGNORECASE,
            )

            if match:

                return match.group(1) + " Years"

        return None