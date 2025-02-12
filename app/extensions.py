from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail

db = SQLAlchemy()
login_manager = LoginManager()
mail = Mail()

def init_login_manager(app):
    login_manager.init_app(app)
    login_manager.login_view = "public_bp.login"  # Asegúrate de que coincide con config.py
    login_manager.login_message = None
