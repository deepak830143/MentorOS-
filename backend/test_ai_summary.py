from app.services.ai_summary_service import AISummaryService

sample = {
    "organization": "APPSC",
    "notification_no": "29/2025",
    "exam_name": "Welfare Organiser",
    "vacancies": 10,
    "salary": "Rs.25,220 - Rs.80,910",
    "age_limit": "45 Years",
    "qualification": (
        "Ex-Service Person, "
        "Intermediate or equivalent, "
        "Able to read/write/speak Telugu."
    ),
    "application_start": "09 Oct 2025",
    "application_end": "29 Oct 2025",
}

summary = AISummaryService.generate(sample)

print()
print("=" * 80)
print(summary)
print("=" * 80)