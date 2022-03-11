from django.urls import reverse_lazy
from django.views import generic as views

from launio.accounts.forms import RegisterForm


class RegisterView(views.CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('show index')
    template_name = 'register.html'
