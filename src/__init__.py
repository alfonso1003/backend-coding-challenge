from flask import Flask


def create_app(script_info=None) -> Flask:
    app = Flask(__name__)
    app.config.from_object("src.config.DevelopmentConfig")

    from flask_restx import Api, Resource

    api: Api = Api(app)

    class Health(Resource):
        def get(self):
            return {"status": "OK", "message": "Server is running"}

    api.add_resource(Health, "/health")

    return app
