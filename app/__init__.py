import os
from flask import Flask
from src.config import MODEL_PATH


def create_app() -> Flask:
    """Create and configure the Flask application instance."""

    # Use app-local static/templates directories
    app = Flask(__name__, static_folder="static", template_folder="templates")

    # Ensure the model directory exists so os.listdir calls in routes do not fail
    os.makedirs(MODEL_PATH, exist_ok=True)

    # Register blueprints
    from app.routes import main  

    app.register_blueprint(main)

    return app


__all__ = ["create_app"]
