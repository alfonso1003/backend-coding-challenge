from flask_restx import Namespace, Resource, reqparse

api = Namespace(
    "suggestions", description="Provide auto-complete suggestions for large cities"
)


class SuggestionList(Resource):
    def post(self):
        """Get a list of auto-complete suggestions based on parameters"""


api.add_resource(SuggestionList, "")
