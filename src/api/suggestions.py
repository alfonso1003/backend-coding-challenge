from flask import request
from flask_restx import Namespace, Resource

from src.cities.services import get_suggestions

api = Namespace(
    "suggestions", description="Provide auto-complete suggestions for large cities"
)


class SuggestionList(Resource):
    @api.doc(
        params={
            "name": {
                "description": "Enter a name for a city",
                "type": "str",
                "default": "New York",
            },
            "lat": {
                "description": "Enter a latitude",
                "type": "float",
                "default": 39.5,  # geographic center of USA
            },
            "long": {
                "description": "Enter a longitude",
                "type": "float",
                "default": 98.35,  # geographic center of USA
            },
        }
    )
    def get(self):
        """Get a list of auto-complete suggestions based on parameters"""
        return get_suggestions(request)


api.add_resource(SuggestionList, "")
