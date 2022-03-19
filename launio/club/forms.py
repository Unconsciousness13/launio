from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from validators.email_validator import UniqueUserEmailField


class AddGymnastForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, label='Nombre')
    last_name = forms.CharField(max_length=30, required=True, label="Apellido")
    photo
    username = forms.CharField(max_length=30, required=True, label='Usuario')

    class Meta:
        model = get_user_model()
        fields = ('username',
                  'first_name',
                  'last_name',
                  'email',
                  'password1',
                  'password2',)
# class CreateContactForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#
#     class Meta:
#         model = Contact
#         fields = ('first_name', 'last_name', 'email', 'phone', 'message')
#
#         labels = {
#             'first_name': 'Nombre',
#             'last_name': 'Apellido',
#             'email': 'Email',
#             'phone': 'Numero de telefono',
#             'message': 'Mensaje',
#         }
#
#         widgets = {
#             "username": forms.TextInput(attrs={
#                 "type": "text", "name": "username", "id": "first_name",
#                 "placeholder": "Username"
#             }),
#             "email": forms.EmailInput(attrs={
#                 "type": "text", "name": "email", "id": "email",
#                 "placeholder": "Email"
#             }),
#
#             "age": forms.NumberInput(attrs={
#                 "type": "number", "name": "age", "id": "age",
#                 "placeholder": "Age", "min": "0"
#             })
#         }
