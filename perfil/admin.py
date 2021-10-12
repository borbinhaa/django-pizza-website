from django.contrib import admin
from . import models


class PerfilInline(admin.TabularInline):
    model = models.Endereco
    extra = 1


class PerfilAdmin(admin.ModelAdmin):
    inlines = [
        PerfilInline
    ]


admin.site.register(models.Perfil, PerfilAdmin)
admin.site.register(models.Endereco)
