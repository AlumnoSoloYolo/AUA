from django.shortcuts import render
from .models import Disco, Merch

# Create your views here.
def listar_discos(request):
    discos = Disco.objects.all()
    return render(request, 'tienda/listar_discos.html', {'discos': discos})


def listar_merch(request):
    merch = Merch.objects.all()
    return render(request, 'tienda/listar_merch.html', {'merch' : merch})