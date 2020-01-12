from django.urls import path
from notaria.datos_basicos import views

app_name = 'datos_basicos'

urlpatterns = [
    path('alta/', views.alta_datos_basicos ,name='alta_datos_basicos'),
    path('listado/', views.listado_datos_basicos, name='listado_datos_basicos'),
    path('editar/<int:datos_basicos_id>', views.editar_datos_basicos, name='editar_datos_basicos')
]