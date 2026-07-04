from app.services.pdf_processing_service import PDFProcessingService

service = PDFProcessingService()

data = service.process(
    "https://psc.ap.gov.in/Documents/NotificationDocuments/WelfareOrganiser_Notification_292025_24092025.pdf"
)

print("\n")
print("=" * 80)
print("PARSED DATA")
print("=" * 80)

for key, value in data.items():
    print(f"{key:20}: {value}")