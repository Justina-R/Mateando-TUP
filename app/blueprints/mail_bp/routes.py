# RUTAS DEL BLUEPRINT  MAIL

from flask import render_template, redirect, url_for, request, current_app
from typing import List, Tuple, Any
from flask_login import login_required, current_user
from app import models
from . import mail_bp
from app.extensions import db, mail
from sqlalchemy import func
from flask_mail import Mail, Message
import random
import string
from dotenv import load_dotenv
import os
import traceback

load_dotenv()


#RUTAS DE CONTACTO

@mail_bp.route('/contacto')
def contacto():
    return render_template('contacto.html')

#Ruta para enviar un mensaje a nuestro mail una vez que el usuario completa el formulario de consulta
@mail_bp.route('/enviarMensaje', methods=['POST'])
def enviar_mensaje(): 

     # Obtener datos del formulario
     nombre = request.form['name']
     apellido = request.form['surname']
     email = request.form['mail']
     mensaje = request.form['mensaje']

     # Crear el mensaje de correo
     msg = Message(
         subject="Nuevo mensaje de contacto",
         sender=os.getenv("MAIL_DEFAULT_SENDER"),
         recipients=[os.getenv("MAIL_USERNAME")]  # Correo del destinatario
     )
     msg.body = f"""
     Nombre: {nombre}
     Apellido: {apellido}
     Correo: {email}

     Mensaje:
     {mensaje}
     """

     try:
         # Enviar el correo
         mail.send(msg)
         print("Mensaje enviado con éxito")
     except Exception as e:
         print(f"Error al enviar el mensaje: {e}")
         print(traceback.format_exc())

     return redirect('/')  # Redirecciona a la página principal

#RUTAS PARA RECUPERAR CONTRASEÑA

@mail_bp.route('/recuperarContrasenia')
def recuperarContrasenia():
    return render_template('/recuperarContrasenia.html')

#Ruta para mandarle un mail al usuario con una contraseña temporal

@mail_bp.route('/enviarContraseniaTemporal', methods=['GET','POST'])
def enviar_contrasenia_temporal():
    email = request.form['email']
    usuario = models.Usuario.query.filter_by(email=email).first()

    if usuario is None:
        mensaje = 'No se encontró un usuario con ese correo electrónico.'
        return render_template('/recuperarContrasenia.html', mensaje=mensaje)
    
    # Genera una contraseña temporal de 8 caracteres
    nueva_contrasenia = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    usuario.set_password(nueva_contrasenia)  # Encriptar la contraseña temporal

    # Guardar la nueva contraseña en la base de datos
    db.session.commit()

    # Crear el mensaje de correo con la nueva contraseña temporal
    msg = Message(
        subject="Recuperación de contraseña - Mateando",
        sender = os.getenv("MAIL_DEFAULT_SENDER"),
        recipients=[email]
    )
    msg.body = f"""
    ¡Hola, {usuario.nombre}!
    
    Has solicitado recuperar tu contraseña. Te hemos asignado una nueva contraseña temporal:
    Cuenta: {email}
    Contraseña temporal: {nueva_contrasenia}

    Te recomendamos cambiar esta contraseña una vez que accedas a tu cuenta.
    ¡No la compartas con nadie!

    Saludos,
    Mateando
    """

    try:
        # Enviar el correo
        mail.send(msg)
        print("Mensaje enviado con éxito")
    except Exception as e:
        print(f"Error al enviar el mensaje: {e}")

    return redirect(url_for('public_bp.index'))