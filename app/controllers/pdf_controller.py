import io

from flask import Blueprint, render_template, request, send_file, session

from app.models.pdf_model import PdfModel

pdf_bp = Blueprint("pdf", __name__)


@pdf_bp.route("/")
def index():
    return render_template("index.html", text=session.get("text"), error=None)


@pdf_bp.route("/cargar", methods=["POST"])
def cargar_pdf():
    uploaded_file = request.files.get("pdf_file")

    if not uploaded_file or uploaded_file.filename == "":
        return render_template("index.html", text=None, error="Debes seleccionar un archivo PDF.")

    if not uploaded_file.filename.lower().endswith(".pdf"):
        return render_template("index.html", text=None, error="El archivo debe ser un PDF.")

    try:
        text = PdfModel.extract_text_from_stream(uploaded_file.stream)
    except Exception:
        return render_template("index.html", text=None, error="No se pudo leer el PDF. Verifica que el archivo no esté dañado.")

    session["text"] = text
    return render_template("index.html", text=text, error=None)


@pdf_bp.route("/exportar-txt")
def exportar_txt():
    text = session.get("text", "")

    buffer = io.BytesIO(text.encode("utf-8"))
    buffer.seek(0)

    return send_file(
        buffer,
        mimetype="text/plain",
        as_attachment=True,
        download_name="contenido_pdf.txt",
    )
