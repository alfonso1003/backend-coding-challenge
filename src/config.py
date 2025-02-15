class Config:
    TESTING = False
    SECRET_KEY = "secretkey!"  # Don't do this in real app!
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///dev-db.sqlite"


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///test-db.sqlite"


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///prod-db.sqlite"
