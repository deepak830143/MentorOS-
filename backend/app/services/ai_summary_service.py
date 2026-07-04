from datetime import date


class AISummaryService:
    """
    Generates a human-readable summary for a notification.
    """

    @staticmethod
    def generate(data: dict) -> str:

        lines = []

        # Notification
        if data.get("notification_no"):
            lines.append(
                f"Notification {data['notification_no']} has been released by {data.get('organization', 'the organization')}."
            )

        # Post
        if data.get("exam_name"):
            lines.append(
                f"The recruitment is for the post of {data['exam_name']}."
            )

        # Vacancies
        if data.get("vacancies"):
            lines.append(
                f"Total vacancies: {data['vacancies']}."
            )

        # Salary
        if data.get("salary"):
            lines.append(
                f"Salary: {data['salary']}."
            )

        # Age
        if data.get("age_limit"):
            lines.append(
                f"Maximum age: {data['age_limit']}."
            )

        # Qualification
        if data.get("qualification"):
            lines.append(
                f"Eligibility: {data['qualification']}"
            )

        # Application Dates
        start = data.get("application_start")
        end = data.get("application_end")

        if start and end:

            if isinstance(start, date):
                start = start.strftime("%d %b %Y")

            if isinstance(end, date):
                end = end.strftime("%d %b %Y")

            lines.append(
                f"Applications are accepted from {start} to {end}."
            )

        return " ".join(lines)