from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('user_name',
                  'first_name',
                  'last_name',
                  'email',
                  'password1',
                  'password2',)
