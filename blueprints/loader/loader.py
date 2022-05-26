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
    picture = request.files.get("picture")
    if not picture:
        logger.error("Файл не загружен")
        return "Файл не загружен", 506
    filename = picture.filename
    extension = filename.split(".")[-1]
    if extension in ALLOWED_EXTENSIONS:
        picture.save(f"{UPLOAD_FOLDER}/{filename}")
    else:
        logger.info("Загруженный файл - не картинка")
        return "Данный тип файла не поддерживается"
    content = request.values.get('content')
    if not content:
        return "Необходимо загрузить текст к посту", 505
    write = write_tag_in_json(f"/uploads/{filename}", content)
    return render_template("post_uploaded.html", filename=filename, content=content)