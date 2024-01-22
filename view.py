from app import app  # из app импортируем app (в нём Flask)


@app.route('/')  # через метод route указываем корень сайта
def index():
    return "Hi"
