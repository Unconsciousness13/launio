from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from validators.email_validator import UniqueUserEmailField

user = get_user_model()


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, label='Nombre')
    last_name = forms.CharField(max_length=30, required=True, label="Apellido")
    email = UniqueUserEmailField(required=True, label='Correo electronico')
    username = forms.CharField(max_length=30, required=True, label='Usuario')

    class Meta:
        model = get_user_model()
        fields = ('username',
                  'first_name',
                  'last_name',
                  'email',
                  'password1',
                  'password2',)

#
# class LoginForm(UserLoginForm):
