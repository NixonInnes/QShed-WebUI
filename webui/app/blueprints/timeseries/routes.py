from datetime import datetime, timedelta
from io import StringIO
import plotly.express as px
from flask import url_for, render_template, request

from bootlets.html import A
from bootlets.boots import Container

from webui.app import client
from webui.app.html.common import Breadcrumb, PageTitle
from webui.app.html.timeseries import TimeseriesRecordHTML, TimeseriesDescribeHTML, TimeseriesPlotHTML
from webui.app.utils.plotting import fig_to_str

from . import timeseries_bp


@timeseries_bp.route("/plot/id/<int:id>")
def plot_by_id(id):
    return plot(id)


@timeseries_bp.route("/plot/<name>")
def plot(name):
    breadcrumb = Breadcrumb(
        A("Home", href=url_for("main.index")),
        "Timeseries",
        name
    )
    title = PageTitle(name)

    start = request.args.get("start")
    if start is None:
        start = datetime.utcnow() - timedelta(days=365)
    else:
        start = datetime.strptime(start, "%Y/%m/%d %H:%M:%S")

    end = request.args.get("end")
    if end is None:
        end = datetime.utcnow()
    else:
        end = datetime.strptime(end, "%Y/%m/%d %H:%M:%S")

    ts = client.ts.get(name, start=start, end=end)

    
    content = TimeseriesPlotHTML(ts)

    
    return render_template(
        "common.html",
        breadcrumb=breadcrumb,
        title=title,
        content=content
    )


@timeseries_bp.route("/test")
def test():
    breadcrumb = Breadcrumb(
        A("Home", href=url_for("main.index")),
        "Timeseries",
        "Test Plot"
    )
    title = PageTitle(f"Test Plot")

    fig = px.scatter(x=range(50))
    content = fig_to_str(fig)
    
    return render_template(
        "common.html",
        breadcrumb=breadcrumb,
        title=title,
        html_content=content
    )


@timeseries_bp.route("/list")
def list():
    breadcrumb = Breadcrumb(
        A("Home", href=url_for("main.index")),
        "Timeseries",
        "List"
    )
    title = PageTitle(f"List")

    records = client.ts.list()
    content = Container(
        *[TimeseriesRecordHTML(record) for record in records]

    )


    return render_template(
        "common.html",
        breadcrumb=breadcrumb,
        title=title,
        content=content
    )