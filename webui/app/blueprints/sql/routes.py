from bootlets.boots import Container, QuickForm
from bootlets.html import A
from flask import abort, render_template, redirect, request, url_for, current_app, flash

from webui.app import client
from webui.app.html.common import Breadcrumb, PageTitle
from webui.app.html.sql_entity import SQLEntityHTML

from . import sql_bp
from .forms import CreateSQLEntityForm


@sql_bp.route("/entity/<int:id>/get", methods=["GET"])
def get_entity(id):
    entity = client.sql.get(id)
    
    if entity is None:
        abort(404)

    breadcrumb = Breadcrumb(
        A("Home", href=url_for("main.index")),
        "SQL Entity",
        entity.name
    )
    title = PageTitle(f"Entity: [{entity.id}] {entity.name}")
    content = SQLEntityHTML(entity)
    
    return render_template(
        "common.html",
        breadcrumb=breadcrumb,
        title=title,
        content=content
    )


@sql_bp.route("/entity/roots", methods=["GET"])
def get_root_entities():
    entities = client.sql.get_roots()

    breadcrumb = Breadcrumb(
        A("Home", href=url_for("main.index")),
        "SQL Entity",
        "Roots"
    )
    title = PageTitle(f"Root Entities")
    content = Container(*[SQLEntityHTML(entity) for entity in entities])

    return render_template(
        "common.html",
        breadcrumb=breadcrumb,
        title=title,
        content=content
    )


@sql_bp.route("/entity/all", methods=["GET"])
def get_all_entities():
    entities = client.sql.get_all()

    breadcrumb = Breadcrumb(
        A("Home", href=url_for("main.index")),
        "SQL Entity",
        "All"
    )
    title = PageTitle(f"All Entities")
    content = Container(*[SQLEntityHTML(entity) for entity in entities])

    return render_template(
        "common.html",
        breadcrumb=breadcrumb,
        title=title,
        content=content
    )


@sql_bp.route("/entity/create", methods=["GET", "POST"])
def create_entity():
    form = CreateSQLEntityForm()

    if form.validate_on_submit():
        entity = client.sql.create(
            name=form.name.data,
            data=form.data.data,
            type_=form.type.data,
            parent=form.parent.data
        )
        flash("New entity created", "success")
        return redirect(url_for("sql.get_entity", id=entity.id))

    breadcrumb = Breadcrumb(
        A("Home", href=url_for("main.index")),
        "SQL Entity",
        "Create"
    )
    title = PageTitle(f"Create Entity")
    content = QuickForm(form)

    return render_template(
        "common.html",
        breadcrumb=breadcrumb,
        title=title,
        content=content
    )
