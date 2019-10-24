from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import config

db = SQLAlchemy()


def create_app(config_name):
    # create app instance
    app = Flask(__name__, static_url_path='/static')

    # apply configuration
    app.config.from_object(obj=config[config_name])
    config[config_name].init_app(app)

    # init extensions
    db.init_app(app)

    # register blueprint
    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api/v1')

    return app
