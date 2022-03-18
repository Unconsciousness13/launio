from django import forms
from django.contrib.auth.models import User


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
