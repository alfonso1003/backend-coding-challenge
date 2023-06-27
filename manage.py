import csv
import sys
from pathlib import Path

from flask.cli import FlaskGroup

from src import create_app, db
from src.cities.models import City  # type: ignore

CITIES_DATA_FILE_PATH = Path("./data/cities_canada-usa.tsv")

app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command("recreate_db")
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command("populate_cities_table")
def populate_cities_table():
    # Set the field size limit to a larger value
    csv.field_size_limit(sys.maxsize)

    with open(CITIES_DATA_FILE_PATH, "r") as file:
        data_reader = csv.reader(file, delimiter="\t")
        next(data_reader)  # Skip header row if needed

        for row in data_reader:
            geoname_id = int(row[0])
            name = row[1]
            country_code = row[8]
            lat = float(row[4])
            long = float(row[5])
            city = City(geoname_id, name, country_code, lat, long)
            db.session.add(city)

        db.session.commit()


if __name__ == "__main__":
    cli()
