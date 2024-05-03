from flask_cors import CORS
import flask
from flask_sqlalchemy import SQLAlchemy
import os

from app import routes


def add_cors(app: flask.Flask):
    CORS(
        app,
        supports_credentials=True,
        resources={
            r"*": {"origins": "*"},
        },
    )


def create_app(env: str) -> flask.Flask:
    app = flask.Flask(__name__)
    app.env = env

    db = SQLAlchemy()
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DATABASE_URI')
    db.init_app(app)
    app.db = db

    app.register_blueprint(routes.bp)
    add_cors(app)

    return app
