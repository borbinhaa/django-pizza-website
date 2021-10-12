from django.contrib import admin
from . import models


class ItemPedidoInline(admin.TabularInline):
    model = models.ItemPedido
    extra = 1


class PedidoAdmin(admin.ModelAdmin):
    inlines = [ItemPedidoInline]
    list_display = ('id', 'status')
    list_editable = ('status',)
    list_filter = ('status',)


admin.site.register(models.ItemPedido)
admin.site.register(models.Pedido, PedidoAdmin)
