from flask import Flask


def create_app() -> Flask:
    app = Flask(__name__, template_folder="views/templates", static_folder="static")
    app.secret_key = "dev-secret-key"

    from app.controllers.pdf_controller import pdf_bp
    app.register_blueprint(pdf_bp)

    from app.controllers.docs_controller import docs_bp
    app.register_blueprint(docs_bp)

    return app
