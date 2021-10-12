from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView
from . import models


class Introducao(ListView):
    model = models.Sabor
    template_name = 'sabores/introducao.html'


class Cardapio(View):
    def get(self, *args, **kwargs):

        sabores_salgados = models.Sabor.objects.filter(
            no_cardapio=True, salgado=True)
        sabores_doce = models.Sabor.objects.filter(no_cardapio=True, doce=True)

        contexto = {
            'sabores_salgados': sabores_salgados,
            'sabores_doces': sabores_doce
        }

        return render(self.request, 'sabores/cardapio.html', contexto)
