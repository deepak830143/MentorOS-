import fitz  # PyMuPDF


class PDFExtractor:
    """
    Extract text from a PDF using PyMuPDF.
    """

    def extract_text(self, pdf_path: str) -> str:

        print(f"📖 Reading PDF : {pdf_path}")

        document = fitz.open(pdf_path)

        full_text = ""

        for page_number in range(len(document)):

            page = document.load_page(page_number)

            full_text += page.get_text()

        document.close()

        print(f"✅ Extracted {len(full_text)} characters")

        return full_text