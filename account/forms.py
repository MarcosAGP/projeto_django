from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = 'username', 'first_name', 'last_name', 'email', 'password1', 'password2'

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Usuário'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Primeiro nome'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Ultimo nome'
        self.fields['email'].widget.attrs['placeholder'] = 'E-mail'
        self.fields['password1'].widget.attrs['placeholder'] = 'Senha'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirme a senha'
        
        
   


