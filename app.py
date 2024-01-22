from flask import Flask
from config import Configuration  # Импортируем настройки

app = Flask(__name__)
app.config.from_object(Configuration)
''' Передаём в словарь config (он есть в Flask) настройки нашего приложения app
 с помощью метода from_object и передаём аргумент Configuration '''
