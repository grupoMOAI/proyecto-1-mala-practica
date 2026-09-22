from typing import BinaryIO

from pypdf import PdfReader


class PdfModel:
    @staticmethod
    def extract_text_from_stream(file_stream: BinaryIO) -> str:
        reader = PdfReader(file_stream)
        pages_text = [page.extract_text() or "" for page in reader.pages]
        return "\n".join(pages_text).strip()
