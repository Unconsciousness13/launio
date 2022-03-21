from django import forms

from launio.club.models import Gymnast


class AddGymnast(forms.ModelForm):
    class Meta:
        model = Gymnast
        fields = ('first_name', 'last_name', 'category', 'train', 'birthdate', 'photo', 'description')

    # widgets = {
    #         'first_name': forms.CharField(attrs={'class': 'add-gymnast-form-inputs'}),
    #         'last_name': forms.CharField(attrs={'class': 'add-gymnast-form-inputs'}),
    #         'category': forms.CharField(attrs={'class': 'add-gymnast-form-inputs'}),
    #         'train': forms.CharField(attrs={'class': 'add-gymnast-form-inputs'}),
    #         'birthdate': forms.DateField(attrs={'class': 'add-gymnast-form-inputs'}),
    #         'photo': forms.ImageField(attrs={'class': 'add-gymnast-form-inputs'}),
    #         'description': forms.Textarea(attrs={'class': 'add-gymnast-form-inputs'}),
    # }

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
