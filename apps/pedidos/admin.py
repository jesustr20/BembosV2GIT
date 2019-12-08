from django.contrib import admin
from .models import Colaborador, Rol, TipoIngrediente, Ingrediente ,EstadoPedido, Pedido, DetallePedido
# Register your models here.

class ColaboradorAdmin(admin.ModelAdmin):
    list_display = ['id','user', 'Localidad', 'edad']

class RolAdmin(admin.ModelAdmin):
    list_display = ['id','rol','colaborador']

class IngredienteAdmin(admin.ModelAdmin):
    list_display = ['id','ingrediente', 'precio', 'cantidad','imagen']

class TipoIngredienteAdmin(admin.ModelAdmin):
    list_display = ['id','nombre','ingrediente']

class EstadoPedidoAdmin(admin.ModelAdmin):
    list_display = ['id','estado']

class DetallePedidoAdmin(admin.ModelAdmin):
    list_display = ['id','ingrediente', 'cantidad', 'precio']

class PedidoAdmin(admin.ModelAdmin):
    list_display = ['id','cliente', 'fecha_pedido', 'monto_total', 'estado', 'atendidopor']


admin.site.register(Colaborador, ColaboradorAdmin)
admin.site.register(Rol, RolAdmin)
admin.site.register(TipoIngrediente, TipoIngredienteAdmin)
admin.site.register(Ingrediente, IngredienteAdmin)
admin.site.register(EstadoPedido, EstadoPedidoAdmin)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(DetallePedido, DetallePedidoAdmin)