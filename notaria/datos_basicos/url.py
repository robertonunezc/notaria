from django.urls import path
from notaria.datos_basicos import views

app_name = 'datos_basicos'

urlpatterns = [
    path('alta/', views.alta_datos_basicos ,name='alta_datos_basicos'),
]