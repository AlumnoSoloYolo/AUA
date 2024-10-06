from django.urls import path
from . import views

urlpatterns = [
    path('discos/', views.listar_discos, name='lista_discos'),
    path('merch/', views.listar_merch, name='lista_merch'),
]