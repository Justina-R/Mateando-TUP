# RUTAS DEL BLUEPRINT ADMIN

from flask import render_template, redirect, url_for, request, Response, jsonify, flash
from typing import List, Tuple, Any
from flask_login import login_required, current_user, logout_user, login_user
from app import models
from . import user_bp
from app.extensions import db
from sqlalchemy import func
import random


#Dirige a la página con los datos del usuario que inició sesión
@user_bp.route('/miPerfil')
@login_required
def miPerfil():
    return render_template('miPerfil.html')

""" Agregar un nuevo Usuario """


@user_bp.route('/addUsuario', methods=["POST"])
def add_usuario() -> Response | str:
    name: str = request.form["name"]
    apellido: str = request.form["surname"]
    email: str = request.form["email"]
    telefono: str = request.form["tel"]
    direccion: str = request.form["direccion"]
    password: str = request.form["password"]


    nuevo_Usuario: models.Usuario = models.Usuario(
        nombre=name, apellido=apellido, email=email, telefono=telefono, direccion=direccion)
    nuevo_Usuario.set_password(password)

    db.session.add(nuevo_Usuario)
    db.session.commit()

    return redirect(url_for("public_bp.index"))


""" Verifica si hay un mail ya registrado -> Lo llama el JS """
@user_bp.route('/verificarEmail', methods=['POST'])
def verificaEmail():
    email = request.json.get('email')
    usuario = models.Usuario.query.filter_by(email=email).first()
    
    if usuario:
        return jsonify({'existe': True})
    else:
        return jsonify({'existe': False})
    

#CARRITO

""" Agregar productos al carrito """
@user_bp.route('/agregaCarrito/<int:id_producto>', methods=["POST"])
@login_required
def agrega_carrito(id_producto: int):
    try:
        usuario = models.Usuario.query.filter_by(id_usuario=current_user.id_usuario).first()

        carrito = models.Carrito.query.filter_by(id_usuario=usuario.id_usuario).first()

        producto = models.Producto.query.filter_by(id_Producto=id_producto).first()

        producto_carrito = models.Producto_Carrito.query.filter_by(id_carrito=carrito.id_carrito, id_producto=producto.id_Producto).first()
 
        if producto_carrito:
            producto_carrito.cantidad += 1
        else:
            nuevo_producto = models.Producto_Carrito(
                id_carrito=carrito.id_carrito,
                id_producto=id_producto,
                cantidad=1,
                precio_unidad=producto.precio
            )
            db.session.add(nuevo_producto)

        db.session.commit()

        
        return redirect(request.referrer)
    except:
        print('Error!')
        return redirect(url_for('public_bp.index'))


# Elimina de carrito
@user_bp.route('/eliminarProductoCarrito/<int:id_Producto_Carrito>', methods=["POST"])
def eliminarProductoCarrito(id_Producto_Carrito: int):
    producto_carrito: models.Producto_Carrito = models.Producto_Carrito.query.get(id_Producto_Carrito)
    if producto_carrito:
        db.session.delete(producto_carrito)
        db.session.commit()
    
    return redirect(request.referrer)


""" Registra una Venta """
@user_bp.route('/venta', methods=["POST"])
def venta():
    usuario = models.Usuario.query.filter_by(id_usuario=current_user.id_usuario).first()
    carrito = models.Carrito.query.filter_by(id_usuario=usuario.id_usuario).first()
    producto_carrito = models.Producto_Carrito.query.filter_by(id_carrito=carrito.id_carrito).all()
    total = db.session.query(
        func.sum(models.Producto_Carrito.precio_unidad * models.Producto_Carrito.cantidad)
    ).filter_by(id_carrito=carrito.id_carrito).scalar()

    nueva_Venta: models.Venta = models.Venta (
        id_carrito = carrito.id_carrito,
        nro_factura = random.randrange(100, 1000),
        total = total
    )

    db.session.add(nueva_Venta)
    for p in producto_carrito:
        db.session.delete(p)
        
    db.session.commit()
    
    return redirect(url_for('public_bp.index'))

#Actualiza los datos del usuario (current_user == FlaskLogin) segun lo ingresado en el form
@user_bp.route('/updateProfile', methods=['GET','POST'])
def updateProfile():

    current_user.nombre = request.form['name']
    current_user.apellido = request.form['surname']
    current_user.email = request.form['email']
    current_user.telefono = request.form['tel']
    current_user.direccion = request.form['direccion']

    db.session.commit()
    return redirect(url_for("public_bp.index"))

@user_bp.route('/verifyPassword', methods=['POST'])
def verificaPasswordOriginal():
    newPassword = request.json.get('newPassword')
    if current_user.check_password(newPassword):
        return jsonify({'contraseniaCorrecta': True})
    else:
        return jsonify({'contraseniaCorrecta': False})

@user_bp.route('/changePassword', methods=["POST"])
def cambiarContraseniaActual():
    try:
        newPassword = request.form['newPassword']
        current_user.set_password(newPassword)
        db.session.commit()
    except Exception as e:
        print(f"Error al modificar la contraseña: {e}")
    return redirect(url_for("user_bp.miPerfil"))

@user_bp.route('/deleteAccount', methods=["POST"])
def deleteAccount():

    db.session.delete(current_user)
    db.session.commit()

    return redirect(url_for("public_bp.index"))

#Ingresar a vista del carrito y enviar los datos del usuario logueado
@user_bp.route('/carrito')
@login_required
def carrito():
    carrito = models.Carrito.query.filter_by(id_usuario=current_user.id_usuario).first()
    productos: List[Tuple[Any]] = models.Producto_Carrito.query.filter_by(id_carrito=carrito.id_carrito).all()
    
    total = db.session.query(
        func.sum(models.Producto_Carrito.precio_unidad * models.Producto_Carrito.cantidad)
    ).filter_by(id_carrito=carrito.id_carrito).scalar()
    
    if not total:
        total = 0
    
    return render_template('carrito.html', productos=productos, total=total)

#Actualiza cantidades dentro del carrito de un usuario
@user_bp.route('/actualizarCantidad', methods=["POST"])
def actualizarCantidad():
    data = request.get_json()
    product_id = data.get("idProducto")
    action = data.get("action")
    
    producto_carrito = models.Producto_Carrito.query.get(product_id)
    if not producto_carrito:
        return jsonify({"success": False}), 404

    if action == "increment":
        producto_carrito.cantidad += 1
    elif action == "decrement" and producto_carrito.cantidad > 1:
        producto_carrito.cantidad -= 1
    
    db.session.commit()
    total = sum(item.cantidad * item.precio_unidad for item in producto_carrito.carrito.productos_carrito)
    
    return jsonify({
        "success": True,
        "newQuantity": producto_carrito.cantidad,
        "newTotal": total
    })

@user_bp.route('/registrarse')
def registrarse():
    return render_template('registrarse.html')

def creaCarrito(usuario):
    carrito = models.Carrito.query.filter_by(id_usuario=current_user.id_usuario).first()
            
    if not carrito:
        nuevoCarrito: models.Carrito = models.Carrito (
            id_usuario = usuario.id_usuario
        )

        db.session.add(nuevoCarrito)
        db.session.commit()


@user_bp.route('/iniciarSesion', methods=['GET', 'POST'])
def iniciarSesion():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        usuario = models.Usuario.query.filter_by(email=email).first()
        
        if usuario and usuario.check_password(password):
            login_user(usuario)  # Usa este método para loguear al usuario
            
            # crear carrito
            creaCarrito(usuario)
                
            return redirect(url_for('admin_bp.dashboard' if usuario.es_admin else 'public_bp.index'))
        else:
            flash("Email o contraseña incorrectos", "danger")
            return redirect(url_for('public_bp.login'))
    
    return redirect(url_for("public_bp.index"))



@user_bp.route('/logout')
def logout():
    logout_user()  # Cierra la sesión del usuario
    # flash("Cierre de sesión exitoso", "info")
    return redirect(url_for('public_bp.index'))