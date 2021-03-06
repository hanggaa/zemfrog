from datetime import timedelta
from os import path

class Development(object):
    SECRET_KEY = "Your secret key!"
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + path.join(
        path.dirname(__file__), "db.sqlite"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = "JWT secret key!"
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=7)
    MAIL_PORT = 8025
    MAIL_DEFAULT_SENDER = "admin@localhost.com"
    APISPEC_TITLE = "API Docs"
    APISPEC_SWAGGER_UI_URL = "/docs"
    DEBUG = True
    {% if main_app -%}
        APPS = []
    {%- endif %}
    EXTENSIONS = [
        "extensions.sqlalchemy",
        "extensions.marshmallow",
        "extensions.migrate",
        "extensions.jwt",
        "extensions.mail",
        "extensions.celery",
        "extensions.apispec",
    ]
    COMMANDS = [
        "zemfrog.commands.api",
        "zemfrog.commands.blueprint",
        "zemfrog.commands.middleware",
        "zemfrog.commands.schema",
        "zemfrog.commands.command",
        {% if main_app -%}
            "zemfrog.commands.app"
        {%- endif %}
    ]
    BLUEPRINTS = ["auth"]
    MIDDLEWARES = []
    APIS = []
    API_DOCS = True
    CREATE_DB = True
    CELERY_RESULT_BACKEND = "redis://127.0.0.1:6379"
    CELERY_BROKER_URL = CELERY_RESULT_BACKEND


class Production(Development):
    DEBUG = False
    JWT_COOKIE_SECURE = True


class Testing(Development):
    TESTING = True
