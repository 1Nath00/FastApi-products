# 🚀 API de Productos con FastAPI
API RESTful para la gestión de productos con autenticación JWT, desarrollada con FastAPI y PostgreSQL.

## 📋 Requisitos
Python 3.10+

PostgreSQL
Pip

## 🛠 Instalación
Clona el repositorio:

bash
Copiar
Editar
git clone https://github.com/1Nath00/FastApi-products.git
cd FastApi-products
Crea y activa un entorno virtual:

bash
Copiar
Editar
python -m venv venv
# Linux / Mac
source venv/bin/activate
# Windows
venv\Scripts\activate
Instala las dependencias:

nginx
Copiar
Editar
pip install -r requirements.txt
Configura la base de datos:

Crea un archivo .env basado en .env.example.

Asegúrate de que PostgreSQL esté corriendo.

Ejecuta las migraciones:

nginx
Copiar
Editar
python -c "from database import Base, engine; Base.metadata.create_all(bind=engine)"
▶️ Ejecución Local
Para correr el proyecto en modo desarrollo:

css
Copiar
Editar
uvicorn main:app --reload
La API estará disponible en:
http://127.0.0.1:8000

# 📚 Documentación Interactiva
Swagger UI: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc

# 🌐 Endpoints
Productos
GET /productos → Lista todos los productos

GET /producto/{id} → Obtiene un producto específico

POST /productos → Crea un nuevo producto

PUT /producto/{id} → Actualiza todos los campos de un producto

PATCH /producto/{id} → Actualiza campos específicos de un producto

DELETE /producto/{id} → Elimina un producto

## 📦 Estructura del Proyecto
bash
Copiar
Editar
FastApi-products/

├── main.py            # Punto de entrada principal

├── database.py        # Configuración de la base de datos

├── models/            # Modelos de SQLAlchemy

│   └── productos.py

├── dtos.py            # Esquemas Pydantic

├── services.py        # Lógica de negocio

├── requirements.txt   # Dependencias

└── .env.example       # Variables de entorno de ejemplo


## 📄 Ejemplos de Requests

Crear producto

makefile

Copiar

Editar

curl -X POST "http://localhost:8000/productos" \

-H "Content-Type: application/json" \

-d '{"nombre": "Laptop", "precio": 1200.99, "cantidad_stock": 10}'

Obtener todos los productos

nginx

Copiar

Editar

curl "http://localhost:8000/productos"

## 🛡️ Variables de Entorno

Variable	Descripción	Valor por defecto

DATABASE_URL	URL de conexión a PostgreSQL	sqlite:///./sql_app.db (ejemplo)

PORT	Puerto donde corre la aplicación	8000
