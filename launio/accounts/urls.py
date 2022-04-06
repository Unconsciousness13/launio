from django.contrib.auth.views import LogoutView
from django.urls import path, reverse_lazy

from launio.accounts.views import UserRegisterView, UserLoginView, ProfilePageView, profile_edit, DeleteProfileView

urlpatterns = (
    path('register/', UserRegisterView.as_view(), name='register page'),
    path('login/', UserLoginView.as_view(), name='login page'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('show index')), name='logout'),
    path('profile/<int:pk>/', ProfilePageView.as_view(), name='profile view'),
    path('profile-edit/<int:pk>/', profile_edit, name='profile edit'),
    path('profile-delete/<int:pk>', DeleteProfileView.as_view(), name='profile delete'),
)
