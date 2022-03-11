from django import forms





#
# class CreateProfileForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#
#     class Meta:
#         model = Profile
#         fields = ('username', 'email', 'age')
#
#         labels = {
#             'username': 'Username',
#             'email': 'Email',
#             'age': 'Age',
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
#             }),
#
#         }
#
#
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
