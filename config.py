import logging

POST_PATH = "posts.json"
UPLOAD_FOLDER = "./uploads/images"
ALLOWED_EXTENSIONS = {'png', 'jpeg', 'jpg'}


logger = logging.getLogger('logger')    # Создаем регистратор
logger.setLevel(logging.INFO)

ch = logging.FileHandler('logger.log')    # Создаем обработчик для файла
ch.setLevel(logging.INFO)   # Установим уровень отладки

strfmt = '[%(asctime)s] [%(name)s] [%(levelname)s] > %(message)s'   # Формируем формат сообщения
datefmt = '%Y-%m-%d %H:%M:%S'   # Формируем индикатор времени сообщения
formatter = logging.Formatter(fmt=strfmt, datefmt=datefmt)  # Создаем форматтер

ch.setFormatter(formatter)  # Добавляем форматтер к обработчику
logger.addHandler(ch)   # Добавляем обработчик в регистратор