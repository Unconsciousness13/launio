from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    class Meta:
        first_name = forms.CharField(max_length=30, required=True, help_text='Campo obligatorio')
        last_name = forms.CharField(max_length=30, required=True, help_text='Campo obligatorio')
        email = forms.EmailField(max_length=254, help_text='Correo electronico tiene que ser valido')

        model = User
        fields = ['first_name',
                  'last_name',
                  'email',
                  'password1',
                  'password2', ]



