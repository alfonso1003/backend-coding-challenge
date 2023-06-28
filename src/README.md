# Note to Reviewer

Thanks for taking a look at my code.

## To Get Started

Create a virtual environment in your preferred method and install the `requirements.txt` file. Then from a terminal, run the following:

```
$ python manage.py recreate_db
$ python manage.py populate_cities_table
$ python manage.py run
```

Navigate to http://127.0.0.1:5000/api/ and test things out. Enjoy!

## What Went Right

I'm very happy with the architecture. I'm experimenting with Flask, SQLAlchemy, and Marshmallow and I'm pretty happy with how that turned out.

## What Went Wrong

My business logic has a very inefficient query that only makes suggestions by name similarity. There were two main issues I came across that prevented me from completing this challenge to my satisfaction:

1. The main issue I had was getting SQLite to work with the spatial and NLP functions.

2. The data file contains 7,237 records. However, the database only loaded 5,339 records. The file might be corrupted, or perhaps there is a limit on SQLite. I would have to explore the file more or try switching to PostgreSQL.

```
$ wc -l data/cities_canada-usa.tsv
    7238 data/cities_canada-usa.tsv

$ select count(*) from cities;
count(*)
5339

```

## Why Not Just Use PostgreSQL Then?

Admittedly, I'm experimenting with these Python Flask packages, and while SQLAlchemy makes it easy to swap out SQLite with PostgreSQL, I wasn't quite able to figure out how to install the fuzzystrmatch and postgis extensions I needed that would have brought the spatial and NLP functions I needed.

If I had succeeded in setting up a PostgreSQL database, then I could have written something like the code below. In the code below, rather than score them, I simplified the requirements to first find cities within 500 miles of the provided coordinates and then narrow those down by city name similarity. I'm not quite sure why an end user would provide both a city name and coordinates, and in a design meeting, I might push back and say the API should provide auto-complete suggestions based on one or the other. I would prefer making suggestions by city name similarity.

```
from sqlalchemy import func
from sqlalchemy.orm import aliased
from fuzzystrmatch import levenshtein

from src import db
from src.cities.models import City
from src.cities.schemas import city_list_schema

DEFAULT_SEARCH_TERMS = {"name": "Abbotsford", "lat": 49.05798, "long": -122.25257}
DISTANCE_THRESHOLD = 500  # miles
SIMILARITY_THRESHOLD = 0.5


def get_suggestions(request):
    name = request.args.get("name", DEFAULT_SEARCH_TERMS["name"])
    lat = float(request.args.get("lat", DEFAULT_SEARCH_TERMS["lat"]))
    lon = float(request.args.get("long", DEFAULT_SEARCH_TERMS["long"]))

    # Calculate the search radius in meters
    search_radius = DISTANCE_THRESHOLD * 1609.34  # Convert miles to meters

    # Perform a spatial query to find cities within the specified radius
    cities_within_radius = City.query.filter(
        func.ST_DWithin(
            func.ST_MakePoint(lon, lat),
            City.coordinates,
            search_radius,
        )
    ).subquery()

    # Perform a query to find cities with similar names using fuzzy string matching
    cities_with_similar_names = db.session.query(City).join(
        cities_within_radius,
        levenshtein(City.name, name) / func.greatest(func.length(City.name), func.length(name))) > SIMILARITY_THRESHOLD
    ).all()

    serialized_data = city_list_schema.dump(cities_with_similar_names)
    return serialized_data, 200
```

## What About Tests?

Normally, I like to test things, but I ran out of time. To see an example of some tests I've written, check out this practice repo of mine:

[https://github.com/alfonso1003/calculator-command-pattern-refactor/

## Final Note

This was a fun assignment and though I have mixed feelings about my final results, I hope you can see the thought I put into the overall design. My intentions for the business logic I think are solid, but I had trouble as explained. In a real-world scenario, this is the kind of stuff that can be figured out, and with a proper database, this would be much easier.

Thanks for considering me, and I hope we can speak soon.
