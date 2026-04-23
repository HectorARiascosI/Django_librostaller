from django.urls import path
from . import views

urlpatterns = [
    # PÁGINA DE INICIO
    path('', views.index, name='index'),
    
    # VISTAS FUNCIÓN
    path('autores/', views.lista_autores, name='lista_autores'),
    path('autores/crear/', views.crear_autor, name='crear_autor'),
    path('autores/editar/<int:pk>/', views.editar_autor, name='editar_autor'),
    path('autores/eliminar/<int:pk>/', views.eliminar_autor, name='eliminar_autor'),
    
    # VISTAS GENÉRICAS
    path('autores/generic/', views.AutorListView.as_view(), name='autor_list_generic'),
    path('autores/generic/crear/', views.AutorCreateView.as_view(), name='autor_create_generic'),
    path('autores/generic/<int:pk>/editar/', views.AutorUpdateView.as_view(), name='autor_update_generic'),
    path('autores/generic/<int:pk>/eliminar/', views.AutorDeleteView.as_view(), name='autor_delete_generic'),

    # VISTAS FUNCIÓN LIBRO
    path('libros/', views.lista_libros, name='lista_libros'),
    path('libros/crear/', views.crear_libro, name='crear_libro'),
    path('libros/editar/<int:pk>/', views.editar_libro, name='editar_libro'),
    path('libros/eliminar/<int:pk>/', views.eliminar_libro, name='eliminar_libro'),

    # VISTAS GENÉRICAS LIBRO
    path('libros/generic/', views.LibroListView.as_view(), name='libro_list_generic'),
    path('libros/generic/crear/', views.LibroCreateView.as_view(), name='libro_create_generic'),
    path('libros/generic/<int:pk>/editar/', views.LibroUpdateView.as_view(), name='libro_update_generic'),
    path('libros/generic/<int:pk>/eliminar/', views.LibroDeleteView.as_view(), name='libro_delete_generic'),
]
