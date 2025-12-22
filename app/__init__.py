from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Создаем экземпляры здесь
db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    # Инициализируем расширения
    db.init_app(app)
    login_manager.init_app(app)
    
    # Импортируем User для login_manager ТОЛЬКО после инициализации
    @login_manager.user_loader
    def load_user(user_id):
        from app.models import User  # Ленивый импорт
        return User.query.get(int(user_id))
    
    # Регистрация blueprints
    from app.routes.main_routes import main_bp
    from app.routes.auth_routes import auth_bp
    from app.routes.api_routes import api_bp
    from app.routes.web_routes import web_bp
    
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(api_bp, url_prefix='/api')
    app.register_blueprint(web_bp)
    
    # Создаем таблицы в контексте приложения
    with app.app_context():
        # Импортируем модели внутри контекста
        from app import models
        db.create_all()
    
    return app
