from flask import Blueprint

nosql_bp = Blueprint("nosql", __name__)

from . import forms, routes
