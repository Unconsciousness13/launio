from django.contrib.auth import get_user_model
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import generic as gen_views
from django.views import generic as views
from django.views.generic import TemplateView

from launio.accounts.forms import RegisterForm, UpdateForm
from launio.accounts.models import NewUser

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
    # permission_required = ('Can add new user', 'Can change new user', 'Can delete new user' 'Can view new user')
    template_name = 'profile/profile.html'

    def get_context_data(self, **kwargs):
        context = super(ProfilePageView, self).get_context_data(**kwargs)
        profile = get_object_or_404(NewUser, **kwargs)
        context['profile'] = profile

        return context


def profile_edit(request, pk):
    profile = NewUser.objects.get(pk=pk)
    if request.method == 'POST':
        form = UpdateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile view', profile.pk)
    else:
        form = UpdateForm(instance=profile)

    context = {
        'form': form,
        'pk': pk,
        'profile': profile,
    }
    return render(request, 'profile/profile-edit.html', context)


class DeleteProfileView(PermissionRequiredMixin, views.DeleteView):
    permission_required = ('Can add new user', 'Can change new user', 'Can delete new user' 'Can view new user')
    model = NewUser
    template_name = 'profile/profile-delete-confirm.html'
    success_url = '/'


# // Errors views //
def handler404(request, exception):
    context = {}
    response = render(request, "errors/404.html", context=context)
    response.status_code = 404
    return response


def handler500(request):
    context = {}
    response = render(request, "errors/500.html", context=context)
    response.status_code = 500
    return response


def handler403(request, exception):
    context = {}
    response = render(request, "errors/403.html", context=context)
    response.status_code = 403
    return response


def handler400(request, exception):
    context = {}
    response = render(request, "errors/400.html", context=context)
    response.status_code = 400
    return response
