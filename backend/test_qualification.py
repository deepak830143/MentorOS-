from app.pdf.extractor import PDFExtractor
from app.extraction.cleaner import TextCleaner
from app.extraction.qualification_extractor import QualificationExtractor

extractor = PDFExtractor()

text = extractor.extract_text(
    "downloads/WelfareOrganiser_Notification_292025_24092025.pdf"
)

text = TextCleaner.clean(text)

qualification = QualificationExtractor.extract(text)

print()

print("=" * 60)

print("Qualification")

print("=" * 60)

print(qualification)