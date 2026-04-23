# 📚 Sistema de Gestión de Libros

Sistema CRUD completo desarrollado en Django para gestionar Autores y Libros.

## 👥 Desarrolladores

- **Hector**: Modelo Autor (CRUD completo)
- **Tatiana**: Modelo Libro (CRUD completo)

## 🚀 Despliegue en Railway

### Paso 1: Crear cuenta en Railway
1. Ve a https://railway.app
2. Inicia sesión con tu cuenta de GitHub

### Paso 2: Crear nuevo proyecto
1. Click en "New Project"
2. Selecciona "Deploy from GitHub repo"
3. Busca y selecciona `Django_librostaller`
4. Railway detectará automáticamente que es un proyecto Django

### Paso 3: Agregar PostgreSQL
1. En tu proyecto, click en "+ New"
2. Selecciona "Database" → "Add PostgreSQL"
3. Railway creará automáticamente la variable `DATABASE_URL`

### Paso 4: Configurar variables de entorno (opcional)
- `DEBUG=False` (para producción)
- `PYTHON_VERSION=3.12`

### Paso 5: Deploy
Railway desplegará automáticamente. El proceso incluye:
- ✅ Instalación de dependencias
- ✅ Migraciones de base de datos
- ✅ Creación de superusuario admin
- ✅ Datos de ejemplo (3 autores, 4 libros)
- ✅ Recolección de archivos estáticos

## 🔐 Credenciales de Admin

```
Usuario: admin
Contraseña: admin123
```

## 🌐 URLs Disponibles

### Página Principal
- `/` - Página de inicio con navegación

### Autores - Vistas Función
- `/autores/` - Lista de autores
- `/autores/crear/` - Crear autor
- `/autores/editar/<id>/` - Editar autor
- `/autores/eliminar/<id>/` - Eliminar autor

### Autores - Vistas Genéricas
- `/autores/generic/` - Lista de autores
- `/autores/generic/crear/` - Crear autor
- `/autores/generic/<id>/editar/` - Editar autor
- `/autores/generic/<id>/eliminar/` - Eliminar autor

### Libros - Vistas Función
- `/libros/` - Lista de libros
- `/libros/crear/` - Crear libro
- `/libros/editar/<id>/` - Editar libro
- `/libros/eliminar/<id>/` - Eliminar libro

### Libros - Vistas Genéricas
- `/libros/generic/` - Lista de libros
- `/libros/generic/crear/` - Crear libro
- `/libros/generic/<id>/editar/` - Editar libro
- `/libros/generic/<id>/eliminar/` - Eliminar libro

### Admin
- `/admin/` - Panel de administración de Django

## 💻 Ejecución Local

### 1. Clonar repositorio
```bash
git clone https://github.com/HectorARiascosI/Django_librostaller.git
cd Django_librostaller
```

### 2. Crear entorno virtual
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Aplicar migraciones
```bash
python manage.py migrate
```

### 5. Crear datos de prueba
```bash
python init_data.py
```

### 6. Ejecutar servidor
```bash
python manage.py runserver
```

### 7. Acceder
- Aplicación: http://localhost:8000
- Admin: http://localhost:8000/admin

## 📋 Características

### Modelo Autor
- Nombre
- Correo (único)
- Nacionalidad
- Fecha de nacimiento
- Biografía (opcional)

### Modelo Libro
- Título
- Fecha de publicación
- Género
- ISBN (único)
- Autor (ForeignKey)

### Funcionalidades
- ✅ CRUD completo con vistas función
- ✅ CRUD completo con vistas genéricas
- ✅ Panel de administración
- ✅ Diseño responsive y profesional
- ✅ Validación de formularios
- ✅ Relación ForeignKey entre modelos

## 🌳 Estructura Git

```
main (producción)
└── dev (desarrollo)
    ├── developer-hector (Autor)
    └── developer-tatiana (Libro)
```

## 🏷️ Versión

**v1.0.0** - Release inicial con CRUD completo

## 📦 Tecnologías

- Django 6.0.4
- PostgreSQL (producción)
- SQLite (desarrollo)
- Gunicorn
- WhiteNoise
- Railway (hosting)

## 📄 Licencia

Proyecto académico - Taller Colaborativo
