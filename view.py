from app import app  # из app.py импортируем app (в нём Flask)
from flask import render_template  # для того чтобы привязать шаблон


@app.route('/')  # через метод route указываем корень сайта ->
def index():
    name = 'Ivan'
    return render_template('index.html', n=name)
