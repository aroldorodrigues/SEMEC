from django.urls import path
from .views import visualizar_dispositivos,editar_dispositivos,adicionar_documento
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('visualizar_dispositivos', visualizar_dispositivos, name='visualizar_dispositivos'),
    path('dispositivos/editar_dispositivo/<int:dispositivo_id>/', editar_dispositivos, name='editar_dispositivos'),
    path('dispositivos/adicionar_documento/<int:dispositivo_id>/', adicionar_documento, name='adicionar_documento')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)