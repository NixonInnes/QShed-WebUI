from flask import flash, redirect, render_template, url_for
from flask_login import current_user, login_user, logout_user, login_required

from bootlets.boots import QuickForm
from bootlets.html import A

from webui.app import db
from webui.app.models import User
from webui.app.html.common import Breadcrumb, PageTitle

from . import auth_bp
from .forms import LoginForm, RegistrationForm


@auth_bp.before_app_request
def before_request():
    if current_user.is_authenticated:
        current_user.ping()


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            flash("You have successfully logged in!", "success")
            return redirect(url_for("main.index"))
        flash("Incorrect username or password!", "warning")

    breadcrumb = Breadcrumb(
        A("Home", href=url_for("main.index")),
        "Login"
    )
    title = PageTitle("Login")
    content = QuickForm(form)
    return render_template(
        "common.html", 
        breadcrumb=breadcrumb,
        title=title,
        content=content
    )


@auth_bp.route("/logout", methods=["GET"])
@login_required
def logout():
    logout_user()
    flash("You are now logged out!", "warning")
    return redirect(url_for("main.index"))


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("You have successfully registered!", "success")
        login_user(user)
        return redirect(url_for("main.index"))
    return render_template("form.html", form=QuickForm(form), title="Register")
