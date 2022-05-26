from django.contrib import admin
from .models import Client
from .models import Pays

@admin.register(Client)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ["id", "nombre", "apellido","correo"]

@admin.register(Pays)
class PaysAdmin(admin.ModelAdmin):
    list_display = ["id","nombre"]
