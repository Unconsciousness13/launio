from django import forms

from launio.club.models import Gymnast, Trainer, NotesTeam, NotesIndividual, Competition


class AddGymnast(forms.ModelForm):
    class Meta:
        model = Gymnast
        fields = ('first_name', 'last_name', 'category', 'train', 'birthdate', 'photo', 'description')
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'category': 'Categoria',
            'train': 'Tipo de entreno',
            'birthdate': 'Fecha de nacimiento',
            'photo': 'Foto',
            'description': 'Descripcion',
        }


class AddTrainer(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = ('first_name', 'last_name', 'train', 'birthdate', 'photo', 'description')

        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'train': 'Categorias que entrena',
            'birthdate': 'Fecha de nacimiento',
            'photo': 'Foto',
            'description': 'Descripcion',
        }


class AddNoteTeam(forms.ModelForm):
    class Meta:
        model: NotesTeam
        fields = '__all__'


class AddNoteIndividual(forms.ModelForm):
    class Meta:
        model: NotesIndividual
        fields = '__all__'


class AddCompetition(forms.ModelForm):
    class Meta:
        model: Competition
        fields = '__all__'
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
