# INCIALIZACIÓN DEL BLUEPRINT DE ADMIN

from flask import Blueprint
mail_bp = Blueprint('mail_bp', __name__, template_folder='templates')

#Importa las rutas definidas en routes.py dentro del contexto del blueprint
from . import routes