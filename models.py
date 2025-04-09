from sqlalchemy import Column, Integer, String
from database import Base

class Productos(Base):
    __tablename__ = "productos"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    precio = Column(Integer, nullable=False)
    cantidad = Column(Integer, nullable=False)