from datetime import datetime, timezone

from src import db


class City(db.Model):
    __tablename__ = "cities"

    id = db.Column(db.Integer, primary_key=True)
    geoname_id = db.Column(db.Integer)
    name = db.Column(db.String(200), nullable=False)
    country_code = db.Column(db.String(200), nullable=False)
    lat = db.Column(db.Float, nullable=False)
    long = db.Column(db.Float, nullable=False)
    created_at = db.Column(
        db.DateTime, default=datetime.now(timezone.utc), nullable=False
    )

    def __init__(
        self, geoname_id: int, name: str, country_code: str, lat: float, long: float
    ):
        self.geoname_id = geoname_id
        self.name = name
        self.country_code = country_code
        self.lat = lat
        self.long = long
