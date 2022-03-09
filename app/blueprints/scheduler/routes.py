import json
from flask import render_template, redirect, url_for

from bootlets.boots import QuickForm

from ... import client
from . import sched_bp
from .forms import NewScheduleForm


@sched_bp.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@sched_bp.route("/list", methods=["GET"])
def list_schedules():
    schedules = client.scheduler.list()
    return render_template("scheduler/list.html", schedules=schedules)


@sched_bp.route("/add", methods=["GET", "POST"])
def add_schedule():
    form = NewScheduleForm()

    if form.validate_on_submit():
        client.scheduler.add(
            interval=form.interval.data,
            url=form.url.data,
            method=form.method.data,
            params=json.loads(form.params.data) if form.params.data else {},
            data=json.loads(form.data.data) if form.data.data else {},
            headers=json.loads(form.headers.data) if form.headers.data else {}
        )
        return redirect(url_for("scheduler.list_schedules"))

    return render_template("form.html", title="New Schedule", form=QuickForm(form))
