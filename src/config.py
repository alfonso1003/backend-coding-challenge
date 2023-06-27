class Config:
    TESTING = False
    SECRET_KEY = "secretkey!"  # Don't do this in real app!
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = "salite:///dev-db.sqlite"


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "salite:///test-db.sqlite"


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "salite:///prod-db.sqlite"
