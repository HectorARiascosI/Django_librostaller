# Guía de Deployment en Render

## Pasos para desplegar en Render

### 1. Preparar el repositorio
✅ Ya está listo - Los archivos de configuración ya están en la rama `developer-tatiana`

### 2. Crear cuenta en Render
1. Ve a [https://render.com](https://render.com)
2. Regístrate con tu cuenta de GitHub

### 3. Crear nuevo Web Service
1. En el dashboard de Render, haz clic en **"New +"** → **"Web Service"**
2. Conecta tu repositorio de GitHub: `HectorARiascosI/Django_librostaller`
3. Selecciona la rama: `developer-tatiana` (o `main` si ya hiciste merge)

### 4. Configurar el Web Service
Usa esta configuración:

- **Name**: `gestion-libros` (o el nombre que prefieras)
- **Region**: Selecciona la más cercana (ej: Oregon, USA)
- **Branch**: `developer-tatiana`
- **Root Directory**: (dejar vacío)
- **Runtime**: `Python 3`
- **Build Command**: `./build.sh`
- **Start Command**: `gunicorn gestion_libros.wsgi:application`

### 5. Variables de entorno
En la sección **Environment**, agrega estas variables:

```
PYTHON_VERSION = 3.11.0
DEBUG = False
SECRET_KEY = (Render lo generará automáticamente, o usa uno propio)
```

### 6. Crear base de datos PostgreSQL (Opcional)
Si quieres usar PostgreSQL en lugar de SQLite:

1. En Render, crea un nuevo **PostgreSQL** database
2. Copia la **Internal Database URL**
3. Agrégala como variable de entorno:
   ```
   DATABASE_URL = postgresql://...
   ```

### 7. Deploy
1. Haz clic en **"Create Web Service"**
2. Render automáticamente:
   - Instalará las dependencias (`requirements.txt`)
   - Ejecutará `collectstatic`
   - Ejecutará las migraciones
   - Iniciará el servidor con Gunicorn

### 8. Acceder a la aplicación
Una vez completado el deploy, Render te dará una URL como:
```
https://gestion-libros.onrender.com
```

### 9. Crear superusuario
Para acceder al admin de Django:

1. En Render, ve a tu Web Service
2. Haz clic en **"Shell"** (terminal)
3. Ejecuta:
   ```bash
   python manage.py createsuperuser
   ```
4. Sigue las instrucciones para crear el usuario

### 10. Acceder al admin
Ve a: `https://tu-app.onrender.com/admin/`

## Rutas disponibles

- `/admin/` - Panel de administración
- `/autores/` - Lista de autores (vista función)
- `/autores/generic/` - Lista de autores (vista genérica)
- `/libros/` - Lista de libros (vista función)
- `/libros/generic/` - Lista de libros (vista genérica)

## Troubleshooting

### Error: "Application failed to respond"
- Verifica que `gunicorn` esté en `requirements.txt`
- Revisa los logs en Render

### Error: "Static files not found"
- Asegúrate que `whitenoise` esté instalado
- Verifica que `collectstatic` se ejecutó en el build

### Error de base de datos
- Si usas PostgreSQL, verifica que `DATABASE_URL` esté configurada
- Si usas SQLite, asegúrate que las migraciones se ejecutaron

## Notas importantes

- **Plan gratuito**: Render tiene un plan gratuito con limitaciones (la app se "duerme" después de 15 min de inactividad)
- **Primera carga**: Puede tardar 30-60 segundos en responder si la app estaba dormida
- **Logs**: Siempre revisa los logs en Render para debugging

## Actualizar la aplicación

Cada vez que hagas `git push` a la rama configurada, Render automáticamente:
1. Detectará los cambios
2. Ejecutará el build
3. Desplegará la nueva versión

¡Listo! Tu aplicación Django está en producción 🚀
