from flask import Flask
from flask_restx import Api, Resource

from src.api import api_bp


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object("src.config.DevelopmentConfig")

    app.register_blueprint(api_bp, url_prefix="/api")

    return app
