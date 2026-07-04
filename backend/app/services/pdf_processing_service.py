from app.pdf.downloader import PDFDownloader
from app.pdf.extractor import PDFExtractor
from app.pdf.parser import PDFParser

from app.extraction.cleaner import TextCleaner


class PDFProcessingService:
    """
    Complete PDF Processing Pipeline

    Download PDF
        ↓
    Extract Text
        ↓
    Clean Text
        ↓
    Parse Fields
    """

    def __init__(self):

        self.downloader = PDFDownloader()

        self.extractor = PDFExtractor()

        self.parser = PDFParser()

    def process(self, pdf_url: str):

        # --------------------------
        # Download PDF
        # --------------------------

        pdf_path = self.downloader.download(pdf_url)

        if not pdf_path:
            return {}

        # --------------------------
        # Extract Text
        # --------------------------

        text = self.extractor.extract_text(pdf_path)

        if not text:
            return {}

        # --------------------------
        # Clean Text
        # --------------------------

        text = TextCleaner.clean(text)

        # --------------------------
        # Parse Information
        # --------------------------

        data = self.parser.parse(text)

        return data