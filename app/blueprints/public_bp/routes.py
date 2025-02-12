# RUTAS DEL BLUEPRINT PUBLIC

from flask import render_template, redirect, url_for, request, Response, jsonify
from typing import List, Tuple, Any
from flask_login import login_required, current_user
from app import models
from . import public_bp
from app.extensions import db
from sqlalchemy import func


# RUTAS DE PRODUCTOS

@public_bp.route('/productos')
def productos():
    productos: List[Tuple[Any]] = models.Producto.query.all()
    return render_template('productos.html', productos=productos)


""" Filtro de productos -> Seccion Productos """
@public_bp.route('/filtrar', methods=["POST"])
def filtrar_productos():
    categorias = request.json.get('categorias', [])
    
    if "todos" in categorias:
        productos_filtrados = models.Producto.query.all()
    else:
        productos_filtrados = models.Producto.query.filter(models.Producto.id_categoria.in_(categorias)).all()
    
    productos_filtrados_json = [
        {
            "id_Producto": p.id_Producto,
            "nombre": p.nombre,
            "precio": p.precio,
            "image_url": p.image_url,
            "id_categoria": p.id_categoria
        }
        
        for p in productos_filtrados
    ]
        
    return jsonify(productos=productos_filtrados_json)


# Ruta de la barra de búsqueda del header
@public_bp.route('/buscar', methods=["GET"])
def buscar_producto():

    # Search es el nombre del input en el HTML
    busqueda = request.args.get('search')

    if busqueda:
        # Realiza una búsqueda en la base de datos usando LIKE para encontrar coincidencias parciales
        productos = models.Producto.query.filter(
            models.Producto.nombre.ilike(f"%{busqueda}%")).all()
    else:
        productos = []  # Si no hay consulta, no devuelve resultados

    return render_template('productos.html', productos=productos)

# Muestra los productos en la página "Productos" según la categoría que elija el cliente en el menú desplegable del nav
@public_bp.route('/productosCat/<int:id_cat>')
def productosCat(id_cat: int):
    productos: List[Tuple[Any]] = models.Producto.query.filter_by(
        id_categoria=id_cat).all()
    return render_template('productos.html', productos=productos)

#Verifica si hay productos (JS)
@public_bp.route('/verificaProductos', methods=['POST'])
@login_required
def verificaProductos():
    usuario = models.Usuario.query.filter_by(id_usuario=current_user.id_usuario).first()
    carrito = models.Carrito.query.filter_by(id_usuario=usuario.id_usuario).first()
    
    cantidad = db.session.query(
            db.func.sum(models.Producto_Carrito.cantidad)
        ).filter_by(id_carrito=carrito.id_carrito).scalar()
    
    return jsonify({"cantidad": cantidad})

#RUTAS BÁSICAS

@public_bp.route('/')
def index():
    productos: List[Tuple[Any]] = models.Producto.query.limit(8).all()
    return render_template("index.html", productos=productos)

@public_bp.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@public_bp.route('/faq')
def faq():
    return render_template('faq.html')


@public_bp.route('/mateTips')
def mateTips():
    return render_template('mateTips.html')


@public_bp.route('/quienesSomos')
def quienesSomos():
    return render_template('quienesSomos.html')

