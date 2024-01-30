from flask import Blueprint

# В переменную posts помещаем конструктор класса Blueprint ->
posts = Blueprint('posts', __name__, template_folder='templates')
