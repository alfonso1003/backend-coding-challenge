from flask_restx import Namespace, Resource

api = Namespace("health", description="Check the health of the app")


class Health(Resource):
    def get(self):
        return {"status": "OK", "message": "Server is running"}


api.add_resource(Health, "")
