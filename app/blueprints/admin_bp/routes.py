# RUTAS DEL BLUEPRINT ADMIN

from flask import render_template, redirect, url_for, request, Response, jsonify
from typing import List, Tuple, Any
from flask_login import login_required, current_user
from app import models
from . import admin_bp
from app.extensions import db
from sqlalchemy import func
from functools import wraps


#Crear decorador que verifique que el usuario que quiere ingresar a la ruta es admin
def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.es_admin:
            return redirect(url_for("public_bp.index"))
        return f(*args, **kwargs)
    return decorated_function


#RUTAS DEL DASHBOARD

#Ingreso al dashboard
@admin_bp.route('/dashboard')
@login_required
@admin_required 
def dashboard():
    
    # Verifica si el usuario es administrador
    if not current_user.es_admin:
        print("No tienes permiso para acceder a esta página.")
        return redirect(url_for('public_bp.index'))  # Redirige al Inicio
    
    # Contador de ventas realizadas -> cuenta todas las tuplas de la tabla Venta
    count = models.Venta.query.count()
    # Suma todos los totales de la tabla Venta y los devuelve como un valor simple (scalar)
    suma = db.session.query(func.sum(models.Venta.total)).scalar()

    if not suma:
        suma = 0
    
    #Guarda todos los productos de la tabla Producto en una lista
    productos: List[Tuple[Any]] = models.Producto.query.all()
    # Solo llega a esta línea si cumple con el atributo es_Admin
    print(productos)
    return render_template("dashboard.html", productos=productos, count= count, suma=suma)

#Agrega un producto a la BBDD
@admin_bp.route('/addProducto', methods=["POST"])
@admin_required
def add_producto() -> Response | str:
    nombre: str = request.form['nombre']
    precio: str = request.form['precio']
    image_url: str = request.form['image_url']
    id_categoria: str = request.form['categoria']

    nuevo_Producto: models.Producto = models.Producto(nombre=nombre, precio=float(
        precio), image_url=image_url, id_categoria=int(id_categoria))
    try:
        db.session.add(nuevo_Producto)
        db.session.commit()
        print("Producto agregado exitosamente")
    except Exception as e:
        # deshace cualquier cambio pendiente en la sesión de la BBDD
        db.session.rollback()
        print(f"Error al agregar el producto: {e}")

    return redirect(url_for("admin_bp.dashboard"))

#Redirecciona a la página para modificar los datos de un producto y envía los datos del producto seleccionado
#BOTÓN "EDITAR"
@admin_bp.route('/editProducto/<int:id_producto>', methods=["POST"])
@admin_required
def editProducto(id_producto: int):
    producto: models.Producto = models.Producto.query.get(id_producto)
    return render_template("editarProducto.html", producto=producto)

#Modifica el producto seleccionado con los cambios ingresados en el formulario
@admin_bp.route('/editarProducto/<int:id_producto>', methods=["POST"])
def edit_producto(id_producto: int) -> Response | str:

    producto: models.Producto = models.Producto.query.get(id_producto)

    producto.nombre = request.form['nombre']
    producto.precio = request.form['precio']
    producto.image_url = request.form['image_url']
    producto.id_categoria = request.form['categoria']

    db.session.commit()
    return redirect(url_for("admin_bp.dashboard"))

#Elimina el producto seleccionado (BOTÓN "ELIMINAR")
@admin_bp.route('/eliminarProducto/<int:id_producto>', methods=["POST"])
@admin_required
def eliminar_producto(id_producto: int) -> Response | str:

    producto: models.Producto = models.Producto.query.get(id_producto)

    if producto:
        db.session.delete(producto)
        db.session.commit()

    return redirect(url_for("admin_bp.dashboard"))

#Busca productos en el dashboard (SIN JS)
@admin_bp.route('/buscarDashboard', methods=["GET"])
@admin_required
def buscar_dashboard():
    busqueda = request.args.get('search')
    if busqueda:
        productos = models.Producto.query.filter(
            models.Producto.nombre.ilike(f"%{busqueda}%")).all()
    else:
        productos = []  # Si no hay consulta, no devuelve resultados

    return render_template('dashboard.html', productos=productos)

#Busca productos en el dashboard (CON JS)
@admin_bp.route('/obtenerProductos', methods=['GET'])
def obtener_productos():
    productos = models.Producto.query.all()
    resultados = [{"id": producto.id_Producto, "nombre": producto.nombre, "precio": producto.precio, "image_url": producto.image_url} for producto in productos]
    return jsonify(resultados)