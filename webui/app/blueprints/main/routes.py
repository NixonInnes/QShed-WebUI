from flask import render_template, redirect, request, url_for, current_app

from webui.app.html.common import Breadcrumb, PageTitle

from . import main_bp


@main_bp.route("/", methods=["GET"])
def index():

    breadcrumb = Breadcrumb("Home")
    title = PageTitle("Home")
    content = None

    
    return render_template(
        "common.html",
        breadcrumb=breadcrumb,
        title=title,
        content=content
    )
