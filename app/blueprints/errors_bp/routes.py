# RUTAS DEL BLUEPRINT ERRORS

from flask import render_template
from . import errors_bp


# Ruta para Errores

@errors_bp.errorhandler(404)
def no_encontrado(error):
    return render_template('error404.html', error=error)


@errors_bp.errorhandler(405)
def method_not_allowed(error):
    return render_template('error405.html', error=error), 405


@errors_bp.errorhandler(500)
def internal_server():
    return render_template('error500.html')
