from app.pdf.extractor import PDFExtractor
from app.services.pdf_parser import PDFParser

extractor = PDFExtractor()

text = extractor.extract_text(
    "downloads/WelfareOrganiser_Notification_292025_24092025.pdf"
)

print()

print("Notification No :", PDFParser.extract_notification_no(text))
print("Vacancies :", PDFParser.extract_vacancies(text))
print("Salary :", PDFParser.extract_salary(text))
print("Age :", PDFParser.extract_age_limit(text))

start, end = PDFParser.extract_application_dates(text)

print("Application Start :", start)
print("Application End :", end)