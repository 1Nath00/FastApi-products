from pydantic import BaseModel
from typing import Optional

class UpdateProducto(BaseModel):
    nombre: Optional[str] = None
    precio: Optional[float] = None
    cantidad_stock: Optional[int] = None
    
class CreatedProducto(BaseModel):
    nombre: str
    precio: float
    cantidad_stock: int