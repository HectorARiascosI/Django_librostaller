import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gestion_libros.settings')
django.setup()

from django.contrib.auth import get_user_model
from gestion.models import Autor, Libro
from datetime import date

User = get_user_model()

# Crear superusuario
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser(
        username='admin',
        email='admin@libros.com',
        password='admin123'
    )
    print('✅ Superusuario creado: admin / admin123')

# Crear autores de ejemplo
autores_data = [
    {
        'nombre': 'Gabriel García Márquez',
        'correo': 'gabo@example.com',
        'nacionalidad': 'Colombiano',
        'fecha_nacimiento': date(1927, 3, 6),
        'biografia': 'Escritor colombiano, premio Nobel de Literatura 1982'
    },
    {
        'nombre': 'Isabel Allende',
        'correo': 'isabel@example.com',
        'nacionalidad': 'Chilena',
        'fecha_nacimiento': date(1942, 8, 2),
        'biografia': 'Escritora chilena, autora de La casa de los espíritus'
    },
    {
        'nombre': 'Jorge Luis Borges',
        'correo': 'borges@example.com',
        'nacionalidad': 'Argentino',
        'fecha_nacimiento': date(1899, 8, 24),
        'biografia': 'Escritor argentino, maestro del cuento corto'
    }
]

for autor_data in autores_data:
    if not Autor.objects.filter(correo=autor_data['correo']).exists():
        Autor.objects.create(**autor_data)
        print(f'✅ Autor creado: {autor_data["nombre"]}')

# Crear libros de ejemplo
libros_data = [
    {
        'titulo': 'Cien años de soledad',
        'fecha_publicacion': date(1967, 5, 30),
        'genero': 'Realismo mágico',
        'isbn': '978-0307474728',
        'autor': Autor.objects.get(correo='gabo@example.com')
    },
    {
        'titulo': 'El amor en los tiempos del cólera',
        'fecha_publicacion': date(1985, 9, 5),
        'genero': 'Romance',
        'isbn': '978-0307389732',
        'autor': Autor.objects.get(correo='gabo@example.com')
    },
    {
        'titulo': 'La casa de los espíritus',
        'fecha_publicacion': date(1982, 1, 1),
        'genero': 'Realismo mágico',
        'isbn': '978-1501117015',
        'autor': Autor.objects.get(correo='isabel@example.com')
    },
    {
        'titulo': 'Ficciones',
        'fecha_publicacion': date(1944, 1, 1),
        'genero': 'Ficción',
        'isbn': '978-0802130303',
        'autor': Autor.objects.get(correo='borges@example.com')
    }
]

for libro_data in libros_data:
    if not Libro.objects.filter(isbn=libro_data['isbn']).exists():
        Libro.objects.create(**libro_data)
        print(f'✅ Libro creado: {libro_data["titulo"]}')

print('\n🎉 Datos iniciales creados exitosamente!')
print('👤 Usuario admin: admin')
print('🔑 Contraseña: admin123')
