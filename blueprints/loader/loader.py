from flask import render_template, Blueprint, request
from functions import *
from config import *

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder="templates")


@loader_blueprint.route("/post/", methods=["GET", "POST"])
def page_post_form():
    """ Создание поста """
    return render_template("post_form.html")


@loader_blueprint.route("/post/new/", methods=["GET", "POST"])
def page_post_upload():
    """ Получение данных поста """
    picture = request.files.get("picture")      # Получаем файл
    if not picture:
        logger.error("Файл не загружен")        # Записываем в лог
        return "Файл не загружен", 506      # Выводим ошибку
    filename = picture.filename         # Получаем родное имя файла
    extension = filename.split(".")[-1]     # Получаем расширение файла
    if extension in ALLOWED_EXTENSIONS:     # Проверяем доступность расширения
        picture.save(f"{UPLOAD_FOLDER}/{filename}")     # Сохраняем файл
    else:
        logger.info("Загруженный файл - не картинка")       # Записываем в лог
        return "Данный тип файла не поддерживается"     # Выводим ошибку
    content = request.values.get('content')     # Получаем текст к посту
    if not content:
        return "Необходимо загрузить текст к посту", 505        #Выводим ошибку
    write = write_tag_in_json(f"/uploads/{filename}", content)
    return render_template("post_uploaded.html", filename=filename, content=content)