from django.contrib import admin
from . import models


class LojasAdmin(admin.ModelAdmin):
    list_display = ('estado', 'rua')
    list_display_links = ('estado', 'rua')


admin.site.register(models.Lojas, LojasAdmin)
