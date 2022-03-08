from django.shortcuts import render, redirect

from launio.club.forms import CreateProfileForm
from launio.club.models import Profile


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None


def show_index(request):
    profile = get_profile()
    if not profile:
        return redirect('register page')

    context = {
        'profile': profile,
    }
    return render(request, 'home-as-guest.html', context)


def show_contact(request):
    return render(request, 'contact.html')


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
