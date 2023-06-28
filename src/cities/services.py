from rapidfuzz import fuzz

from src import db
from src.cities.models import City
from src.cities.schemas import city_list_schema


def get_suggestions(request):
    name = request.args.get("name")

    # Query the database for cities
    cities = City.query.all()

    # Calculate the similarity ratio for each city name
    results = [(city, fuzz.ratio(name, city.name)) for city in cities]

    # Sort the results by the similarity ratio in descending order
    sorted_results = sorted(results, key=lambda x: x[1], reverse=True)

    # Limit the results to 10 cities
    limited_results = sorted_results[:10]

    # Extract city data from the limited results
    city_data = [city for city, _ in limited_results]

    # Serialize the city data using the schema
    serialized_data = city_list_schema.dump(city_data)

    return serialized_data, 200
