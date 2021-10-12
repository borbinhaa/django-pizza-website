from django import forms
from django.contrib.auth.models import User
from . import models


class EnderecoForm(forms.ModelForm):
    class Meta:
        model = models.Endereco
        fields = '__all__'
        exclude = ('perfil',)


class PerfilForm(forms.ModelForm):
    class Meta:
        model = models.Perfil
        fields = '__all__'
        exclude = ('user',)


class UserForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(),
        label='Senha:'
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(),
        label='Confirmar Senha'
    )

    username = forms.CharField(
        widget=forms.TextInput(),
        label='Usuário',
    )

    first_name = forms.CharField(
        widget=forms.TextInput(),
        label='Nome',
        required=True
    )

    last_name = forms.CharField(
        widget=forms.TextInput(),
        label='Sobrenome',
        required=True
    )

    email = forms.CharField(
        widget=forms.EmailInput(),
        label='Email',
        required=True
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'password', 'password2', 'email')

    def clean(self, *args, **kwargs):
        data = self.cleaned_data

        validation_error_messages = {}

        usuario_data = data.get('username')
        email_data = data.get('email')
        password_data = data.get('password')
        password2_data = data.get('password2')

        usuario_db = User.objects.filter(username=usuario_data).first()
        email_db = User.objects.filter(email=email_data).first()

        erros_msg_user_exists = 'Usuário já existe'
        erros_msg_email_exists = 'Email já existe'
        erros_msg_password_match = 'As duas senhas não conferem'
        erros_msg_password_short = 'Sua senha precisa ter no mínimo 6 '\
            'carácteres'

        if usuario_db:
            validation_error_messages['username'] = erros_msg_user_exists

        if email_db:
            validation_error_messages['email'] = erros_msg_email_exists

        if len(str(password_data)) < 6:
            validation_error_messages['password'] = erros_msg_password_short

        if not password_data == password2_data:
            validation_error_messages['password'] = erros_msg_password_match

        if validation_error_messages:
            raise forms.ValidationError(validation_error_messages)

        return super().clean()
