from django.contrib import admin

# Register your models here.

from .models import PaginaInicio, Libros, Pedidos, solicitudes


class LibrosAdmin(admin.ModelAdmin):
  list_display=("isb", "nombre", "imagen", "disponible")

class PedidosAmind(admin.ModelAdmin):
  list_display=("numeroOrden", "nombre", "telefono", "correo")

class SolicitudesAdmin(admin.ModelAdmin):
  list_display=("nombre", "telefono", "correo", "detalle")
  

admin.site.register(PaginaInicio)
admin.site.register(Libros, LibrosAdmin)
admin.site.register(Pedidos)
admin.site.register(solicitudes)