from django.urls import path
from . import views

app_name = 'perfil'

urlpatterns = [
    path('', views.Login.as_view(), name='login'),
    path('cadastro/', views.Cadastro.as_view(), name='cadastro'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('perfil/', views.ShowPerfil.as_view(), name='perfil'),
    path('perfil/endereco', views.AddEndereco.as_view(), name='add_endereco')
]
