from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.views import generic as gen_views
from django.views.generic import DetailView

from launio.accounts.forms import RegisterForm
from launio.accounts.models import Profile


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


# class ProfilePageView(DetailView):
#     model = Profile
#     template_name = 'profile/profile.html'
#
#     def get_context_data(self,*args, **kwargs):
#         users = Profile.objects.all()
#         context = super(ProfileView, self).get_context_data(**kwargs)
#         context['profile'] = Profile.objects.all(id=Profile.pk)
