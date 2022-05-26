from flask import render_template, Blueprint, request, abort
from functions import *
from config import *


main_blueprint = Blueprint('main_blueprint', __name__, template_folder="templates")


@main_blueprint.route("/")
def page_index():
    return render_template("index.html")


@main_blueprint.route("/list/")
def page_tag():
    try:
        content = request.args.get('content')
        search = search_by_tag(content)
        if not content:
            return "Строка поиска пустая", 506
        elif not search:
            return "Нет таких постов", 505
        logger.info("Выполняется поиск")
    except (FileNotFoundError, json.JSONDecodeError):
        abort(500, description="File error")
    return render_template("post_list.html", search=search, content=content)


