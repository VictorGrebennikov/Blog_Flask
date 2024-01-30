from flask import Flask
from config import Configuration  # Импортируем настройки
from posts.blueprint import posts  # Импортируем Blueprint ->

app = Flask(__name__)
app.config.from_object(Configuration)
''' Передаём в словарь config (он есть в Flask) настройки нашего приложения app
 с помощью метода from_object и передаём аргумент Configuration '''
app.register_blueprint(posts, url_prefix='/blog')  # регистрируем ->
