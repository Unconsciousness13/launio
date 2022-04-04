from django import forms

from launio.club.models import Gymnast, Trainer, NotesTeam, NotesIndividual, Competition, Team, Contact


class AddGymnast(forms.ModelForm):
    class Meta:
        model = Gymnast
        fields = ('first_name', 'last_name', 'category', 'team', 'train', 'birthdate', 'photo', 'description')
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'category': 'Categoria',
            'train': 'Tipo de entreno',
            'team': 'Conjunto',
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
        model = NotesTeam
        fields = ('nota_competition', 'competition', 'team', 'competition_place_on_board')

        labels = {
            'nota_competition': 'Nota',
            'competition': 'Elejir competicion',
            'team': 'Categoria',
            'competition_place_on_board': 'Puesto',
        }


class AddNoteIndividual(forms.ModelForm):
    class Meta:
        model = NotesIndividual
        fields = '__all__'

        labels = {
            'nota_competition': 'Nota',
            'competition': 'Elejir competicion',
            'gymnast': 'Gimnasta',
            'competition_place_on_board': 'Puesto',
        }


class AddCompetition(forms.ModelForm):
    class Meta:
        model = Competition
        fields = '__all__'

        labels = {
            'competition_club_organisation': 'Club organizando la competicion',
            'competition_name': 'Nombre de la competicion',
            'competition_place': 'Lugar(poblacion)',
            'competition_date': 'Fecha de competicion',
        }


class AddTeam(forms.ModelForm):
    class Meta:
        model = Team
        fields = '__all__'


class CreateContactForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Contact
        fields = ('first_name', 'email_address', 'message')

        labels = {
            'first_name': 'Nombre',
            'email': 'Email',
            'message': 'Mensaje',
        }
