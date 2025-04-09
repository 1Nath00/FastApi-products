from fastapi import FastAPI, Depends
from typing import  Annotated
import os

import models
import services
from dtos import CreatedProducto, UpdateProducto
from database import SessionLocal, engine
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(bind=engine)
    
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_denpency = Annotated[Session, Depends(get_db)]

@app.get("/productos")
def get_productos(db: db_denpency):
    return services.findAll(db)

@app.post("/productos")
def create_producto(producto: CreatedProducto, db: db_denpency):
    return services.create(db, producto) 

@app.get("/producto/{id}")
def get_producto(id: int, db: db_denpency):
    return services.find(id, db)

@app.put("/producto/{id}")
def update_producto(id: int, producto: CreatedProducto, db: db_denpency):
    return services.update(id, db, producto)

@app.patch("/producto/{id}")
def patch_producto(id: int, producto: UpdateProducto, db: db_denpency):
    return services.update(id, db, producto)

@app.delete("/producto/{id}")
def delete_producto(id: int, db: db_denpency):
    return services.delete(id, db)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))