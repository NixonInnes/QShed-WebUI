from flask import Blueprint

sched_bp = Blueprint("scheduler", __name__)

from . import forms, routes
