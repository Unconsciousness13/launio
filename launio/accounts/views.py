from django.contrib.auth import get_user_model
from django.contrib.auth import views as auth_views
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import generic as gen_views
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
    template_name = 'profile/profile.html'

    def get_context_data(self, **kwargs):
        context = super(ProfilePageView, self).get_context_data(**kwargs)
        profile = get_object_or_404(NewUser, **kwargs)
        context['profile'] = profile

        return context


# class ProfileEditView(gen_views.UpdateView):
#     model = get_user_model()
#     form_class = RegisterForm
#     template_name = 'profile/profile-edit.html'
#     context_object_name = 'NewUser'
#
#     def get_success_url(self):
#         pk = self.kwargs["pk"]
#         return reverse("profile view", kwargs={"pk": pk})
#     # success_url = f'/profile/{profile.pk}'


# def profile_edit_view(request, id):
#     instance = get_object_or_404(NewUser, id=id)
#     form = UpdateForm(request.POST or None, instance=instance)
#     if form.is_valid():
#         form.save()
#         return redirect('profile view')
#     return render(request, 'profile/profile-edit.html', {'form': form})


# class ProfileEditView(gen_views.UpdateView):
#     template_name = 'profile/profile-edit.html'
#     context_object_name = 'NewUser'
#     model = NewUser
#     form_class = UpdateForm
#
#     def get_success_url(self):
#         return reverse('profile view', kwargs={'pk': self.get_object().id})
#
#     def get_context_data(self, **kwargs):
#         profile = NewUser.objects.get(id)
#         context = super(ProfileEditView, self).get_context_data(**kwargs)
#         context['user_form'] = UpdateForm(instance=self.object.profile)
#         return context

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
