from django.contrib.auth.views import LogoutView
from django.urls import path, reverse_lazy

from launio.accounts.views import UserRegisterView, UserLoginView, ProfilePageView

urlpatterns = (
    path('register/', UserRegisterView.as_view(), name='register page'),
    path('login/', UserLoginView.as_view(), name='login page'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('show index')), name='logout'),

)
