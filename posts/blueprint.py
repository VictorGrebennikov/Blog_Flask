from flask import Blueprint
from flask import render_template  # импортируем функцию render_template

# В переменную posts помещаем конструктор класса Blueprint ->
posts = Blueprint('posts', __name__, template_folder='templates')


@posts.route('/')  # Создаём вьюху
def index():
    return render_template(
        'posts/index.html')  # имя шаблона из posts\template\posts
