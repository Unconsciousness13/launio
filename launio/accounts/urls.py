from django.urls import path

from launio.accounts.views import UserRegisterView, UserLoginView

urlpatterns = (
    path('register/', UserRegisterView.as_view(), name='register page'),
    path('login/', UserLoginView.as_view(), name='login page')
)
