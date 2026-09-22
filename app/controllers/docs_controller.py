from flask import Blueprint, render_template

from app.models.docs_model import DocsModel

docs_bp = Blueprint("docs", __name__)


@docs_bp.route("/docs")
def index():
    error = None
    content_html = ""
    try:
        content_html = DocsModel.get_html()
    except FileNotFoundError as exc:
        error = str(exc)

    return render_template("docs.html", content_html=content_html, error=error)
