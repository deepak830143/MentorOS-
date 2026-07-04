from app.pdf.downloader import PDFDownloader
from app.pdf.extractor import PDFExtractor
from app.pdf.parser import PDFParser


pdf_downloader = PDFDownloader()

pdf_path = pdf_downloader.download(
    "https://psc.ap.gov.in/Documents/NotificationDocuments/WelfareOrganiser_Notification_292025_24092025.pdf"
)

extractor = PDFExtractor()

text = extractor.extract_text(pdf_path)

parser = PDFParser()

data = parser.parse(text)

print("\n")
print("=" * 80)
print("PARSED DATA")
print("=" * 80)

for key, value in data.items():
    print(f"{key:20}: {value}")