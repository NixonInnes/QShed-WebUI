import yaml
from flask import render_template, redirect, request, url_for, current_app

from ... import client
from . import sched_bp


@sched_bp.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@sched_bp.route("/list", methods=["GET"])
def list_schedulers():
    schedulers = client.scheduler.list()
    schedulers = [yaml.dump(scheduler) for scheduler in schedulers]
    return render_template("scheduler/list.html", schedulers=schedulers)
