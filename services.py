import models
from fastapi import HTTPException


def find(id, db):
    producto = db.query(models.Productos).filter(models.Productos.id == id).first()
    
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    
    return producto

def findAll(db):
    productos = db.query(models.Productos).all()
    
    if not productos:
        raise HTTPException(status_code=404, detail="No hay productos")
    
    return productos

def create(db, producto):
    db_producto = models.Productos(
                                    nombre=producto.nombre, 
                                    precio=producto.precio, 
                                    cantidad=producto.cantidad_stock)
    db.add(db_producto)
    db.commit()
    db.refresh(db_producto) 
    
    return db_producto

def update(id, db, producto):
    db_producto = find(id, db)
    
    if producto.nombre:
        db_producto.nombre = producto.nombre
    if producto.precio:
        db_producto.precio = producto.precio
    if producto.cantidad_stock:
        db_producto.cantidad = producto.cantidad_stock
    
    db.commit()
    db.refresh(db_producto)
    
    return db_producto

def delete(id, db):
    db_producto = find(id, db)
    
    db.commit()
    db.delete(db_producto)
    
    return "Producto eliminado correctamente"