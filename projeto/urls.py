# projeto/urls.py 
from django.contrib import admin 
from django.urls import path, include 
from django.conf import settings # <--- Importe settings 
from django.conf.urls.static import static # <--- Importe static 
urlpatterns = [ 
path('admin/', admin.site.urls), 
path('receitas/', include('receitas.urls')), 
] 
# Configuração para servir arquivos de mídia (imagens, etc.) no modo de desenvolvimento 
# IMPORTANTE: Isso é APENAS para desenvolvimento. NÃO use em produção. 
if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, 
document_root=settings.MEDIA_ROOT)