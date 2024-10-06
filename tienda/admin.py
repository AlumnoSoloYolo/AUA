from django.contrib import admin

# Register your models here.
from .models import Disco
from.models import Merch

@admin.register(Disco)
class DiscoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descripcion')

admin.site.register(Merch)