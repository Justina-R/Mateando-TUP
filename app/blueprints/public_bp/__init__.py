#INICIALIZACIÓN DE BLUEPRINT USER

from flask import Blueprint
public_bp = Blueprint('public_bp', __name__, template_folder='templates')

#Importa las rutas definidas en routes.py dentro del contexto del blueprint
from . import routes