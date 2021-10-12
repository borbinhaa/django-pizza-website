from django.urls import path
from . import views

app_name = 'sabores'


urlpatterns = [
    path('', views.Introducao.as_view(), name='introducao'),
    path('cardapio/', views.Cardapio.as_view(), name='cardapio'),
]
