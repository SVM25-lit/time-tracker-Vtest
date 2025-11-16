from flask import Blueprint, render_template

# Создаем Blueprint
main_routes = Blueprint('main_routes', __name__)

@main_routes.route('/')
def index():
    return render_template('index.html')

@main_routes.route('/schedule')
def schedule():
    return "Страница расписания - скоро здесь будет расписание!"

@main_routes.route('/test')
def test():
    return "✅ Тестовая страница работает!"