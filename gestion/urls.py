from django.urls import path
from . import views

urlpatterns = [
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
]
