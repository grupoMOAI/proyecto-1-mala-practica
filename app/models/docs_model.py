from pathlib import Path

import markdown

DOCS_PATH = Path(__file__).resolve().parent.parent.parent / "docs" / "manual-usuario.md"


class DocsModel:
    @staticmethod
    def get_html() -> str:
        if not DOCS_PATH.exists():
            raise FileNotFoundError(f"No se encontró el manual: {DOCS_PATH}")

        text = DOCS_PATH.read_text(encoding="utf-8")
        return markdown.markdown(text, extensions=["tables"])
