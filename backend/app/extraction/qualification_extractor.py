import re


class QualificationExtractor:
    """
    Extract only the actual educational qualification requirements.
    """

    @staticmethod
    def extract(text: str):

        # Find the qualification block
        match = re.search(
            r"No person shall be eligible for appointment.*?unless;(.*?)(?=Note:|PARA-|ANNEXURE|SYLLABUS|SCHEME OF EXAMINATION)",
            text,
            re.IGNORECASE | re.DOTALL,
        )

        if not match:
            return None

        qualification = match.group(1)

        # Normalize whitespace
        qualification = re.sub(r"\s+", " ", qualification).strip()

        return qualification