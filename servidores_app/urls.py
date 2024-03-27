# nome_do_app/urls.py
from django.urls import path
from .views import visualizar_usuarios,cadastrar_usuarios,editar_usuario,criar_usuario

urlpatterns = [
    path('visualizar_usuarios/', visualizar_usuarios, name='visualizar_usuarios'),
    path('cadastrar_usuarios/', cadastrar_usuarios, name='cadastrar_usuarios'),
    path('editar_usuario/<int:usuario_id>/', editar_usuario, name='editar_usuario'),
    path('criar_usuario/', criar_usuario, name='criar_usuario'),
]
