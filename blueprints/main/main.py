from flask import render_template, Blueprint, request, abort
from functions import *
from config import *


main_blueprint = Blueprint('main_blueprint', __name__, template_folder="templates")


@main_blueprint.route("/")
def page_index():
    """ Отображение главной страницы """
    return render_template("index.html")


@main_blueprint.route("/list/")
def page_tag():
    """ Поиск по тегу """
    try:
        content = request.args.get('content')   # Получаем тег по строковому вводу
        search = search_by_tag(content)     # Получаем результат функции
        if not content:
            return "Строка поиска пустая", 506      # Выводим ошибку
        elif not search:
            return "Нет таких постов", 505      # Выводим ошибку
        logger.info("Выполняется поиск")        # Записываем в лог
    except (FileNotFoundError, json.JSONDecodeError):
        abort(500, description="File error")        #Выводим ошибку
    return render_template("post_list.html", search=search, content=content)


