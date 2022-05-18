import os
from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

from qshed.client import QShedClient

from config import config


csrf = CSRFProtect()
db = SQLAlchemy()
config = config[os.getenv("APP_CONFIG", "default")]
login_manager = LoginManager()
client = QShedClient(config.GATEWAY_ADDRESS)


def create_app():
    app = Flask(__name__)

    config.init_app(app)
    csrf.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.session_protection = "strong"
    login_manager.login_view = "auth.login"
    Migrate(app, db)

    from .blueprints.main import main_bp as main_blueprint
    from .blueprints.auth import auth_bp as auth_blueprint
    from .blueprints.nosql import nosql_bp as nosql_blueprint
    from .blueprints.scheduler import sched_bp as scheduler_blueprint
    from .blueprints.sql import sql_bp as sql_blueprint

    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint, url_prefix="/auth")
    app.register_blueprint(nosql_blueprint, url_prefix="/nosql")
    app.register_blueprint(scheduler_blueprint, url_prefix="/scheduler")
    app.register_blueprint(sql_blueprint, url_prefix="/sql")

    return app
