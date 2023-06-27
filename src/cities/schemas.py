from src import ma
from src.cities.models import City


class CitySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = City
        load_instance = True
        ordered = True


city_list_schema = CitySchema(many=True)
