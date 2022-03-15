from django.urls import reverse_lazy
from django.views import generic as gen_views
from django.contrib.auth import views as auth_views

from launio.accounts.forms import RegisterForm


class UserRegisterView(gen_views.CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('show index')
    template_name = 'register.html'


class UserLoginView(auth_views.LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('show index')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()
