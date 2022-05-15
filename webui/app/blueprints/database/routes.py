import yaml
import json
from flask import render_template, redirect, request, url_for, current_app

from ... import client
from . import data_bp


@data_bp.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@data_bp.route("/list", methods=["GET"])
def list_databases():
    databases = client.nosql.list()
    return render_template("database/list.html", databases=databases)

@data_bp.route("/<database_name>/", methods=["GET"])
def show_database(database_name):
    collections = client.nosql[database_name].list()
    return render_template("database/database.html", database_name=database_name, collections=collections)

@data_bp.route("/<database_name>/<collection_name>", methods=["GET"])
def show_collection(database_name, collection_name):
    documents = client.nosql[database_name][collection_name].data
    try:
        documents = [yaml.dump(document) for document in json.loads(documents)]
    except:
        documents = ["Error: Unable to parse JSON"]
    return render_template("database/collection.html", database_name=database_name, collection_name=collection_name, documents=documents)
