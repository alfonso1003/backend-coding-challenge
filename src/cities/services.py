from src import db
from src.cities.models import City
from src.cities.schemas import city_list_schema


def get_suggestions(request):
    # TODO: fun part! business logic
    # name similarity use haversine distance
    # to get distances, use geoalchemy2 and coordinates
    name = request.args.get("name")
    lat = request.args.get("lat")
    long = request.args.get("long")
    return city_list_schema.dump(City.query.limit(10).all()), 200
