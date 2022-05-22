from flask import Blueprint

timeseries_bp = Blueprint("timeseries", __name__)

from . import routes
