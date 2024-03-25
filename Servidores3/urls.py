# nome_do_projeto/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('servidores/', include('servidores_app.urls')),
    path('programas', include('escolas_conectadas_app.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
