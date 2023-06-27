from flask import Blueprint
from flask_restx import Api

from src.api.health import api as health_ns

api_bp = Blueprint("api", __name__)

api = Api(api_bp, title="Flask REST API", description="REST API built with Flask")

api.add_namespace(health_ns)
