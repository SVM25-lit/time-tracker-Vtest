from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///time_tracker.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your-secret-key'

db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test')
def test():
    return "Тестовая страница, к счастью, работает!"

@app.route('/schedule')
def schedule():
    return "Расписания пока нет, но насторй бешеный"

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print("База данных создана!")
        print("Сервер запускается...")
        print("Откройте: http://localhost:5000")
    
    app.run(debug=True, port=5000)