# nome_do_app/urls.py
from django.urls import path
from .views import verificar
urlpatterns = [
    path('medidor', verificar, name='programas'),
    
]