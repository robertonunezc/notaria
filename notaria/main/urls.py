from django.urls import path
from notaria.main import views

app_name = 'main'

urlpatterns = [
    path('', views.dashboard ,name='dashboard'),
]
