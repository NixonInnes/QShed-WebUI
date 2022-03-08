import os
from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

from qshed.client import QShedClient

from config import config


csrf = CSRFProtect()
db = SQLAlchemy()
config = config[os.getenv("APP_CONFIG", "default")]
login_manager = LoginManager()
moment = Moment()
client = QShedClient("http://localhost:5000")


def create_app():
    app = Flask(__name__)

    config.init_app(app)
    csrf.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.session_protection = "strong"
    login_manager.login_view = "auth.login"
    Migrate(app, db)
    moment.init_app(app)

    if not app.debug and not app.testing:
        try:
            from flask.ext.sslify import SSLify

            sslify = SSLify(app)
            app.logger.info("SSL enabled")
        except:
            pass

    from .blueprints.main import main_bp as main_blueprint
    from .blueprints.auth import auth_bp as auth_blueprint
    from .blueprints.database import data_bp as database_blueprint
    from .blueprints.scheduler import sched_bp as scheduler_blueprint

    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint, url_prefix="/auth")
    app.register_blueprint(database_blueprint, url_prefix="/database")
    app.register_blueprint(scheduler_blueprint, url_prefix="/scheduler")

    return app
