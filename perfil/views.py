from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.views import View
from . import forms, models
from django.contrib import messages


class BaseView(View):
    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)

        self.contexto = {
            'userform': forms.UserForm(data=self.request.POST or None),
            'enderecoform': forms.EnderecoForm(data=self.request.POST or None),
            'perfilform': forms.PerfilForm(data=self.request.POST or None),
        }

        self.userform = self.contexto['userform']
        self.enderecoform = self.contexto['enderecoform']
        self.perfilform = self.contexto['perfilform']

        self.renderizar = render(
            self.request, 'perfil/cadastro.html', self.contexto)

    def is_all_valid(self):
        return (self.userform.is_valid() and self.enderecoform.is_valid() and
                self.perfilform.is_valid())

    def get(self, *args, **kwargs):
        return self.renderizar


class Login(View):
    def get(self, *args, **kwargs):
        return render(self.request, 'perfil/login.html')

    def post(self, *args, **kwargs):

        usuario = self.request.POST.get('usuario')
        senha = self.request.POST.get('password')

        autenticacao = authenticate(
            self.request, username=usuario, password=senha)

        if not autenticacao:
            messages.error(
                self.request,
                'Usuário e/ou senha inválidos'
            )
            return render(self.request, 'perfil/login.html')

        login(self.request, user=autenticacao)

        if not self.request.session.get('carrinho'):
            self.request.session['carrinho'] = {}

        messages.success(
            self.request,
            'Login feito com sucesso'
        )

        return redirect('sabores:introducao')


class Logout(View):
    def get(self, *args, **kwargs):
        logout(self.request)
        messages.success(
            self.request,
            'Logout realizado com sucesso.'
        )
        return redirect('sabores:introducao')


class ShowPerfil(BaseView):
    def get(self, *args, **kwargs):

        user = self.request.user
        perfil: models.Perfil = models.Perfil.objects.filter(
            user=user.id).first()

        contexto = {
            'user': user,
            'perfil': perfil,
        }

        return render(self.request, 'perfil/showperfil.html', contexto)


class Cadastro(BaseView):
    def post(self, *args, **kwargs):
        if not self.is_all_valid():
            messages.error(
                self.request,
                'Formulário preenchido incorretamente'
            )
            return self.renderizar

        password = self.userform.cleaned_data.get('password')

        usuario = self.userform.save(commit=False)
        usuario.set_password(password)
        usuario.save()

        perfil = self.perfilform.save(commit=False)
        perfil.user = usuario
        perfil.save()

        endereco = self.enderecoform.save(commit=False)
        endereco.perfil = perfil
        endereco.save()

        messages.success(
            self.request,
            'Cadastro efetuado com sucesso.'
        )

        return redirect('perfil:login')


class AddEndereco(ShowPerfil):
    def get(self, *args, **kwargs):
        return render(self.request, 'perfil/add_endereco.html', self.contexto)

    def post(self, *args, **kwargs):
        if not self.enderecoform.is_valid():
            return render(self.request, 'perfil/add_endereco.html',
                          self.contexto)

        perfil: models.Perfil = models.Perfil.objects.filter(
            user=self.request.user.id).first()

        endereco = self.enderecoform.save(commit=False)
        endereco.perfil = perfil
        endereco.save()

        messages.success(
            self.request,
            'Endereço adicionado com sucesso.'
        )

        return redirect('perfil:perfil')
