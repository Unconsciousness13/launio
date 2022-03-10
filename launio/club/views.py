from django.contrib.auth import forms as auth_forms
from django.contrib.auth import views as auth_views
from django.shortcuts import render, redirect
from django.views import generic as views

from launio.club.forms import CreateProfileForm
from launio.club.models import Profile


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None


def show_index(request):
    profile = get_profile()
    # if not profile:
    #     return redirect('show index')

    context = {
        'profile': profile,
    }
    return render(request, 'home.html', context)


def show_contact(request):
    profile = get_profile()
    if not profile:
        return redirect('register page')

    context = {
        'profile': profile,
    }
    return render(request, 'contact.html', context)


def register_user(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show index')

    else:
        form = CreateProfileForm()

    context = {
        'form': form,
        'no_profile': True,
    }
    return render(request, 'register.html', context)


def login_user(request):
    return render(request, 'login.html')


# def contact_page(request):

def trainers(request):
    profile = get_profile()
    if not profile:
        return redirect('register page')

    context = {
        'profile': profile,
    }
    return render(request, 'trainers.html', context)


def gymnasts(request):
    profile = get_profile()
    if not profile:
        return redirect('register page')

    context = {
        'profile': profile,
    }
    return render(request, 'gymnasts.html', context)


def directors(request):
    profile = get_profile()
    if not profile:
        return redirect('register page')

    context = {
        'profile': profile,
    }
    return render(request, 'directors.html', context)


# Classes


class UserLogoutView(auth_views.LogoutView):
    pass
#
#
# class UserRegistrationView(views.CreateView):
#     form_class = auth_forms.UserCreationForm
#     template_name = 'register.html'
