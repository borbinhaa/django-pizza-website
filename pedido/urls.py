from django.urls import path
from . import views

app_name = 'pedido'

urlpatterns = [
    path('', views.Carrinho.as_view(), name='carrinho'),
    path('fazerpedido/', views.FazerPedido.as_view(), name='fazerpedido'),
    path('meuspedidos/', views.MeusPedidos.as_view(), name='meuspedidos'),
    path('removerdocarrinho/', views.RemoveCarrinho.as_view(),
         name='removerdocarrinho'),
    path('confirmarpedido/', views.ConfirmarPedido.as_view(),
         name='confirmarpedido')
]
