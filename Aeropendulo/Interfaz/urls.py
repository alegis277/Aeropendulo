from django.urls import path
from django.urls import include, re_path
from django.views.generic.base import RedirectView
from . import views

favicon_view = RedirectView.as_view(url='/static/favicon.png', permanent=True)

urlpatterns = [
    path('', views.index, name='index'),
    path('actualizarDatos', views.actualizarDatos, name='actualizarDatos'),
    path('entrada_req', views.entrada_req, name='entrada_req'),
    
]