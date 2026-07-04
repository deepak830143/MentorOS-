import re


class TextCleaner:
    """
    Cleans extracted PDF text before parsing.
    """

    @staticmethod
    def clean(text: str) -> str:

        if not text:
            return ""

        # Windows line endings
        text = text.replace("\r", "\n")

        # Tabs
        text = text.replace("\t", " ")

        # Normalize dashes
        text = text.replace("–", "-")
        text = text.replace("—", "-")

        # Remove multiple spaces
        text = re.sub(r"[ ]{2,}", " ", text)

        # Remove multiple blank lines
        text = re.sub(r"\n{2,}", "\n", text)

        # Remove page numbers
        text = re.sub(r"\n\s*\d+\s*\n", "\n", text)

        return text.strip()