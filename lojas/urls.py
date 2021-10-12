from django.urls import path
from . import views

app_name = 'loja'


urlpatterns = [
    path('', views.Lojas.as_view(), name='lojas'),
]
