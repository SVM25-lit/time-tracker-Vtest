from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Создаем экземпляры ТОЛЬКО здесь
db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    # Инициализируем расширения
    db.init_app(app)
    login_manager.init_app(app)
    
    # Устанавливаем login view
    login_manager.login_view = 'auth.login'
    
    # Регистрация blueprints
    from app.routes.main_routes import main_bp
    from app.routes.auth_routes import auth_bp
    from app.routes.api_routes import api_bp
    from app.routes.web_routes import web_bp
    
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(api_bp, url_prefix='/api')
    app.register_blueprint(web_bp)
    
    # Импортируем модели и настраиваем user_loader внутри контекста
    with app.app_context():
        # Импортируем модели
        from app.models import User
        
        # Настраиваем user_loader
        @login_manager.user_loader
        def load_user(user_id):
            return User.query.get(int(user_id))
        
        # Создаем таблицы
        db.create_all()
    
    return app
