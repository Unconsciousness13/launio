from django.views import generic as views

from launio.club.models import Trainer, Gymnast


class HomeView(views.TemplateView):
    template_name = 'home.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['hide_additional_nav_items'] = True
    #     return context
    #
    # def dispatch(self, request, *args, **kwargs):
    #     if request.user.is_autenticated:
    #         return redirect('dashboard')
    #     return super().dispatch(request, *args, **kwargs)


class EntrenadorasView(views.ListView):
    model = Trainer
    template_name = 'trainers.html'
    ordering = 'birthdate', 'train'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class GymnastsView(views.ListView):
    model = Gymnast
    template_name = 'gymnasts.html'
    ordering = 'birthdate', 'first_name'


class AddGymnastView(views.FormView):
    pass


class AddTrainerView(views.FormView):
    pass
