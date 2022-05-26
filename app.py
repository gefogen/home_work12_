from flask import Flask, request, render_template, send_from_directory, abort
from functions import *
from blueprints.main.main import main_blueprint
from blueprints.loader.loader import loader_blueprint
from config import *

app = Flask(__name__)


app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)


@app.route("/uploads/<path:path>", methods=["GET", "POST"])
def static_dir(path):
    return send_from_directory(UPLOAD_FOLDER, path)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('error404.html', title="Страница не найдена", error=error), 404


@app.errorhandler(500)
def error_handle(e):
    return str(e)


if __name__ == "__main__":
    app.run(debug=True)
