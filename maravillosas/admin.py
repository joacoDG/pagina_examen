from django.contrib import admin
from .models import Empresa, Comuna, Region, Pagina, Carrito, Producto, Usuario
# Register your models here.

admin.site.register(Empresa)
admin.site.register(Comuna)
admin.site.register(Region)
admin.site.register(Pagina)
admin.site.register(Carrito)
admin.site.register(Producto)
admin.site.register(Usuario)
