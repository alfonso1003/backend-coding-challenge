from flask import request
from flask_restx import Namespace, Resource

from src.cities.services import get_suggestions

GEOGRAPHIC_CENTER_OF_US = {"latitude": 39.5, "longitude": 98.35}

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
                "default": GEOGRAPHIC_CENTER_OF_US["latitude"],
            },
            "long": {
                "description": "Enter a longitude",
                "type": "float",
                "default": GEOGRAPHIC_CENTER_OF_US["longitude"],
            },
        }
    )
    def get(self):
        """Get a list of auto-complete suggestions based on parameters"""
        return get_suggestions(request)


api.add_resource(SuggestionList, "")
