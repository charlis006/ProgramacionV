# 📚 Proyecto Librería

Sistema web para la gestión de una librería, desarrollado con Django. Permite administrar libros, usuarios, reportes y autenticación.

---

## 🚀 Funcionalidades principales

- Gestión de libros (altas, bajas, modificaciones).
- Módulo de autenticación (usuarios y permisos).
- Generación de reportes.
- Interfaz web amigable y adaptable.

---

## 🛠 Tecnologías utilizadas

- Python 3.12.10
- Django 5.2.1
- HTML / CSS / Bootstrap (opcional)
- PostgreSQL (o SQLite en desarrollo)
- VSCode como entorno de desarrollo

---

## 🧪 Instalación y ejecución

1. Clonar el repositorio:


git clone https://github.com/charlis006/ProgramacionV.git

cd proyecto_libreria

2. Crear y activar entorno virtual:

python -m venv env
source env/bin/activate  # En Windows: env\Scripts\activate


5. Instalar dependencias:

- pip install -r requirements.txt

7. Configurar el archivo .env con tus variables de entorno:

- SECRET_KEY=tu_clave_secreta

- DEBUG=True

- DB_NAME=nombre_bd

- DB_USER=usuario

- DB_PASSWORD=contraseña

- DB_HOST=localhost


9. Realizar migraciones y ejecutar el servidor:

- python manage.py migrate

- python manage.py runserver


📁 Estructura del proyecto
---

proyecto_libreria/

├── accounts/           # Módulo de usuarios

├── libros/             # Módulo de gestión de libros

├── reportes/           # Reportes del sistema

├── proyecto_libreria/  # Configuración general del proyecto Django

├── requirements.txt    # Dependencias del proyecto

├── manage.py           # Script principal de Django

└── .env                # Variables de entorno (no subido al repo)


👤 Autor
---

Carlos Alcaraz – @tuusuario

Copyright (c) 2025 Carlos Alcaraz


