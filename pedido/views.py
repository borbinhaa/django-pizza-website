from django.contrib.auth.models import User
from django.http.response import Http404
from perfil.models import Endereco, Perfil
from .models import ItemPedido, Pedido
from typing import Dict, List
from django.shortcuts import redirect, render
from django.views import View
from sabores import models
from django.contrib import messages


class Carrinho(View):
    def get(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('perfil:login')

        carrinho: Dict = self.request.session.get('carrinho')
        total = ''

        if carrinho:
            total = self.get_total()

        contexto: Dict = {
            'carrinho': carrinho,
            'total': total
        }

        return render(self.request, 'pedido/carrinho.html', contexto)

    def get_total(self):
        return sum(
            [x['preco']
             if type(x) == dict
             else 0
             for x
             in list(self.request.session['carrinho'].values())
             ]
        )


class RemoveCarrinho(View):
    def get(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('perfil:login')

        self.carrinho: Dict = self.request.session.get('carrinho')
        self.sabor: str = self.request.GET.get('vid')
        key = self.get_deleted_key()
        http_referer = self.request.META.get('HTTP_REFERER')

        if not self.carrinho or not self.sabor:
            return redirect('pedido:fazerpedido')

        try:
            del self.carrinho[key]
        except:
            raise Http404

        self.request.session.save()

        return redirect(http_referer)

    def get_deleted_key(self):
        keys: List = [
            k if v['sabor'] == self.sabor else None
            for k, v in self.carrinho.items()
        ]

        for key in keys:
            if key is not None:
                return key


class ConfirmarPedido(Carrinho):
    def get(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('perfil:login')

        carrinho: Dict = self.request.session.get('carrinho')

        if not carrinho:
            return redirect('pedido:fazerpedido')

        user: User = self.request.user
        perfil: Perfil = Perfil.objects.filter(user=user.id).first()
        enderecos: Endereco = Endereco.objects.filter(perfil=perfil)
        total: float = self.get_total()

        contexto: Dict = {
            'carrinho': carrinho,
            'total': total,
            'enderecos': enderecos
        }

        return render(self.request, 'pedido/confirmar_pedido.html', contexto)

    def post(self, *args, **kwargs):
        user_id = self.request.user.id
        perfil: Perfil = Perfil.objects.filter(user=user_id).first()
        endereco_id: str = self.request.POST.get('endereco')
        endereco_db: Endereco = Endereco.objects.filter(id=endereco_id).first()
        endereco: str = f'{endereco_db.rua}, n {endereco_db.numero}, '\
            f'{endereco_db.cidade}'

        carrinho = self.request.session.get('carrinho')

        pedido: Pedido = Pedido(
            perfil_pedido=perfil,
            endereco=endereco,
            total=self.get_total(),
            status='P',
        )
        pedido.save()

        ItemPedido.objects.bulk_create(
            [
                ItemPedido(
                    pedido=pedido,
                    sabor=pizza['sabor'],
                    tamanho=pizza['tamanho'],
                    quantidade=pizza['quantidade'],
                    preco=pizza['preco'],
                )
                for pizza in carrinho.values()
            ]
        )

        del self.request.session['carrinho']

        messages.success(
            self.request,
            'Pedido realizado com sucesso. Agradecemos a preferência.'
        )
        return redirect('pedido:meuspedidos')


class MeusPedidos(View):
    def get(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('perfil:login')

        user_id = self.request.user.id
        perfil: Perfil = Perfil.objects.filter(user=user_id).first()
        pedidos: Pedido = Pedido.objects.filter(
            perfil_pedido=perfil)

        contexto: Dict = {
            'pedidos': pedidos,
        }
        
        return render(self.request, 'pedido/meus_pedidos.html', contexto)


class FazerPedido(View):
    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)

        sabores_salgados: models.Sabor = models.Sabor.objects.filter(
            no_cardapio=True, salgado=True)

        sabores_doces: models.Sabor = models.Sabor.objects.filter(
            no_cardapio=True, doce=True)

        self.contexto: Dict = {
            'sabores_salgados': sabores_salgados,
            'sabores_doces': sabores_doces,
        }

        self.renderizar = render(
            self.request, 'pedido/fazer_pedido.html', self.contexto)

    def get(self, *args, **kwargs):
        return self.renderizar

    def post(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('perfil:login')

        http_referer = self.request.META.get('HTTP_REFERER')
        datas: Dict = self.request.POST
        self.carrinho = self.request.session.get('carrinho')
        self.tamanho: str = datas.get('size')
        self.quantidade: int = 1
        sabores_id: List = []

        for k, v in datas.items():
            if 'sabor' in k:
                sabores_id.append(int(v))

        if not self.tamanho:
            messages.error(
                self.request,
                'Precisa selecionar um tamanho',
            )
            return redirect(http_referer)

        if self.is_2_flavors():
            if len(datas) != 4:
                messages.error(
                    self.request,
                    'Selecione 2 sabores'
                )
                return redirect(http_referer)

            self.sabor1 = models.Sabor.objects.filter(id=sabores_id[0]).first()
            self.sabor2 = models.Sabor.objects.filter(id=sabores_id[1]).first()
            self.sabor = f'{self.sabor1} e {self.sabor2}'
            self.sabor_id = str(sum(sabores_id)) + self.sabor2.nome_sabor

        if self.is_1_flavor():
            if len(datas) != 3:
                messages.error(
                    self.request,
                    'Selecione apenas 1 sabor'
                )
                return redirect(http_referer)
            self.sabor1 = models.Sabor.objects.filter(id=sabores_id[0]).first()
            self.sabor = f'{self.sabor1}'
            self.sabor_id = str(sum(sabores_id))

        if not self.carrinho:
            self.request.session['carrinho'] = {}
            self.carrinho = self.request.session['carrinho']

        if self.sabor_id in self.carrinho.keys():
            self.carrinho[self.sabor_id]['quantidade'] += 1

            preco = self.get_preco()

            self.carrinho[self.sabor_id]['preco'] = round(preco, 2)
        else:

            preco = self.get_preco()
            tamanho = self.get_size()

            self.carrinho[self.sabor_id] = {
                'sabor': self.sabor,
                'tamanho': tamanho,
                'quantidade': self.quantidade,
                'preco': round(preco, 2)
            }

        self.request.session.save()

        messages.success(
            self.request,
            'Pizza adicionada ao carrinho. Vá ate lá para finalizar o pedido.'
        )
        return redirect('pedido:fazerpedido')

    def get_preco(self):
        tamanho: str = self.tamanho
        quantidade: int = self.quantidade
        if self.sabor_id in self.carrinho:
            quantidade = self.carrinho[self.sabor_id]['quantidade']

        if 'grande' in tamanho:
            if self.is_1_flavor():
                preco = self.sabor1.preco_grande * quantidade

            if self.is_2_flavors():
                preco = ((self.sabor1.preco_grande +
                         self.sabor2.preco_grande) / 2 * quantidade)

        if 'media' in tamanho:
            if self.is_1_flavor():
                preco = self.sabor1.preco_medio * quantidade

            if self.is_2_flavors():
                preco = ((self.sabor1.preco_medio +
                         self.sabor2.preco_medio) / 2 * quantidade)

        if 'pequena' in tamanho:
            if self.is_1_flavor():
                preco = self.sabor1.preco_pequeno * quantidade

            if self.is_2_flavors():
                preco = ((self.sabor1.preco_pequeno +
                         self.sabor2.preco_pequeno) / 2 * quantidade)

        return preco

    def get_size(self):
        if 'grande' in self.tamanho:
            return 'Pizza Grande'

        if 'media' in self.tamanho:
            return 'Pizza Media'

        return 'Pizza Pequena'

    def is_2_flavors(self):
        return '2' in self.tamanho

    def is_1_flavor(self):
        return '1' in self.tamanho
