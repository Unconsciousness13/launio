from django.contrib.auth import get_user_model
from django.contrib.auth import views as auth_views
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic as gen_views
from django.views.generic import TemplateView

from launio.accounts.forms import RegisterForm

User = get_user_model()


class UserRegisterView(gen_views.CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('login page')
    template_name = 'profile/register.html'


class UserLoginView(auth_views.LoginView):
    template_name = 'profile/login.html'
    success_url = reverse_lazy('show index')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class ProfilePageView(TemplateView):
    template_name = 'profile/profile.html'

    def get_context_data(self, **kwargs):
        context = super(ProfilePageView, self).get_context_data(**kwargs)
        profile = get_object_or_404(User, **kwargs)
        context['profile'] = profile

        return context
