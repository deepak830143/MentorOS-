import re
from urllib.parse import urljoin

from bs4 import BeautifulSoup

from app.collectors.appsc.config import APPSC_BASE_URL


class APPSCParser:
    """
    Parser for APPSC Recruitment Notifications.
    """

    def parse(self, html: str):

        soup = BeautifulSoup(html, "html.parser")

        notifications = []

        container = soup.select_one("div.text_a")

        if container is None:
            print("❌ Notification container not found.")
            return notifications

        links = container.select("ul li a")

        print(f"✅ Found {len(links)} notification links.")

        for link in links:

            title = link.get_text(" ", strip=True)

            if not title:
                continue

            href = link.get("href", "").strip()

            # -----------------------------------
            # Convert Relative URL → Absolute URL
            # -----------------------------------
            pdf_url = urljoin(APPSC_BASE_URL, href)

            # -----------------------------------
            # Skip unwanted links
            # -----------------------------------
            lower_title = title.lower()

            if (
                "old information" in lower_title
                or "2018-2019" in lower_title
                or "2019-2020" in lower_title
                or "2020-2021" in lower_title
            ):
                continue

            # -----------------------------------
            # Notification Number
            # -----------------------------------
            notification_no = None

            match = re.search(
                r"Notification\s+No\.?\s*([0-9]+/[0-9]+)",
                title,
                re.IGNORECASE,
            )

            if match:
                notification_no = match.group(1)

            # -----------------------------------
            # Notification Date
            # -----------------------------------
            notification_date = None

            match = re.search(
                r"Dated[: ]*([0-9]{2}[./][0-9]{2}[./][0-9]{4})",
                title,
                re.IGNORECASE,
            )

            if match:
                notification_date = match.group(1)

            # -----------------------------------
            # Post Name
            # -----------------------------------
            post_name = None

            match = re.search(
                r"Post of (.+?) in ",
                title,
                re.IGNORECASE,
            )

            if match:
                post_name = match.group(1).strip()

            # -----------------------------------
            # Recruitment Type
            # -----------------------------------
            recruitment_type = None

            match = re.search(
                r"\((.*?)\)\s*$",
                title,
            )

            if match:
                recruitment_type = match.group(1).strip()

            print("=" * 80)
            print("TITLE :", title)
            print("HREF  :", href)
            print("URL   :", pdf_url)

            notifications.append(
                {
                    "notification_no": notification_no,
                    "notification_date": notification_date,
                    "post_name": post_name,
                    "recruitment_type": recruitment_type,
                    "title": title,
                    "pdf_url": pdf_url,
                }
            )

        return notifications