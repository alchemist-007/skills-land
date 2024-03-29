from flask import Flask
from config import config
from flask_sqlalchemy  import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from pymongo import MongoClient

bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    db.init_app(app)
    login_manager.init_app(app)
    bootstrap.init_app(app)

    return app
