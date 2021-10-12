from django.contrib import admin
from . import models


class SaborAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_sabor', 'no_cardapio', 'doce', 'salgado')
    list_editable = ('no_cardapio', 'doce', 'salgado')
    list_filter = ('no_cardapio',)
    list_display_links = ('id', 'nome_sabor')


admin.site.register(models.Sabor, SaborAdmin)
