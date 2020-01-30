from django.urls import path
from notaria.main import views
from notaria.datos_basicos import views as views_notarias

app_name = 'main'

urlpatterns = [
    #path('', views.dashboard ,name='dashboard'),
    path('', views_notarias.alta_datos_basicos,name='alta_datos_basicos'),
]
