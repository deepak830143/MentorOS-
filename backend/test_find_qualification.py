from app.pdf.extractor import PDFExtractor
from app.extraction.cleaner import TextCleaner

extractor = PDFExtractor()

text = extractor.extract_text(
    "downloads/WelfareOrganiser_Notification_292025_24092025.pdf"
)

text = TextCleaner.clean(text)

keywords = [
    "qualification",
    "educational",
    "degree",
    "bachelor",
    "diploma",
    "mbbs",
    "bhms",
    "b.tech",
    "b.e",
    "essential",
    "must possess",
]

for keyword in keywords:

    index = text.lower().find(keyword)

    if index != -1:

        print("=" * 80)
        print(f"FOUND : {keyword}")
        print("=" * 80)

        start = max(index - 300, 0)
        end = min(index + 1000, len(text))

        print(text[start:end])
        print("\n")