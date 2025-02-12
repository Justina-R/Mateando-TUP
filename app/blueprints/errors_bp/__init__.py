# INCIALIZACIÓN DEL BLUEPRINT DE ERRORS

from flask import Blueprint
errors_bp = Blueprint('errors_bp', __name__, template_folder='templates')

#Importa las rutas definidas en routes.py dentro del contexto del blueprint
from . import routes