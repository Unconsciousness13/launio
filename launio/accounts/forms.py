from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

user = get_user_model()


class UniqueUserEmailField(forms.EmailField):

    def validate(self, value):
        super(forms.EmailField, self).validate(value)
        if User.objects.filter(email=value).exists():
            raise forms.ValidationError("Usuario con este correo electronico ya existe")
        # try:
        #     User.objects.get(email=value)
        #     raise forms.ValidationError("Email already exists")
        # except User.MultipleObjectsReturned:
        #     raise forms.ValidationError("Email already exists")


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
