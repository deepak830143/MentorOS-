import os
import requests


class PDFDownloader:
    """
    Downloads government notification PDFs.
    """

    DOWNLOAD_DIR = "downloads"

    def __init__(self):

        os.makedirs(self.DOWNLOAD_DIR, exist_ok=True)

    def download(self, pdf_url: str):

        if not pdf_url:
            return None

        filename = pdf_url.split("/")[-1]

        filepath = os.path.join(
            self.DOWNLOAD_DIR,
            filename,
        )

        # Already downloaded
        if os.path.exists(filepath):

            print(f"📄 Already Exists : {filename}")

            return filepath

        print(f"⬇ Downloading : {filename}")

        response = requests.get(
            pdf_url,
            timeout=60,
        )

        response.raise_for_status()

        with open(filepath, "wb") as file:

            file.write(response.content)

        print(f"✅ Saved : {filepath}")

        return filepath