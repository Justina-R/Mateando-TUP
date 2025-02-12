# INCIALIZACIÓN DEL BLUEPRINT DE ADMIN

from flask import Blueprint
admin_bp = Blueprint('admin_bp', __name__, template_folder='templates')

#Importa las rutas definidas en routes.py dentro del contexto del blueprint
from . import routes