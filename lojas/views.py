from django.shortcuts import render
from django.views import View
from . import models


class Lojas(View):
    def get(self, *args, **kwargs):

        lojas_sc = models.Lojas.objects.filter(estado='SC')
        lojas_sp = models.Lojas.objects.filter(estado='SP')
        lojas_rj = models.Lojas.objects.filter(estado='RJ')

        contexto = {
            'lojas_sc': lojas_sc,
            'lojas_rj': lojas_rj,
            'lojas_sp': lojas_sp,
        }

        return render(self.request, 'lojas/loja.html', contexto)
