import hashlib


def generate_notification_hash(
    source: str,
    organization: str,
    exam_name: str,
    notification_no: str | None,
    title: str,
) -> str:
    """
    Generate a unique SHA256 hash for a notification.
    """

    text = (
        f"{source}|"
        f"{organization}|"
        f"{exam_name}|"
        f"{notification_no}|"
        f"{title}"
    )

    return hashlib.sha256(text.encode()).hexdigest()