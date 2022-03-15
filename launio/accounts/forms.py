from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

user = get_user_model()


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Campo obligatorio')
    last_name = forms.CharField(max_length=30, required=True, help_text='Campo obligatorio')
    email = forms.EmailField(max_length=254, help_text='Correo electronico tiene que ser valido')
    username = forms.CharField(max_length=30, required=True, help_text='Campo obligatorio')

    class Meta:
        model = get_user_model()
        fields = ['username',
                  'first_name',
                  'last_name',
                  'email',
                  'password1',
                  'password2', ]

    # def clean(self, *args, **kwargs):
    #     email = self.cleaned_data.get('email')
    #     email_user = user.objects.filter(email=email)
    #     if email_user.exist():
    #         raise forms.ValidationError('User with this  email already exist')
    #     return super(UserCreationForm, self).clean(*args, **kwargs)
