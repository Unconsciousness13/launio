from django.shortcuts import render


def get_profile(pk):
    # profile = Profile.objects.get(pk=Profile.pk)
    # if profile:
    #     return profile
    # return None
    pass


def show_index(request):
    # profile = get_profile(pk)
    # if not profile:
    #     return redirect('create profile')
    #
    # context = {
    #     'profile': profile,
    #     'pk': pk,
    #
    # }
    # return render(request, 'home-as-guest.html', context)
    return render(request, 'home-as-guest.html')
