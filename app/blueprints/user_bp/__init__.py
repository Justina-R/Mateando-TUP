# INCIALIZACIÓN DEL BLUEPRINT DE USER

from flask import Blueprint
user_bp = Blueprint('user_bp', __name__, template_folder='templates')

#Importa las rutas definidas en routes.py dentro del contexto del blueprint
from . import routes