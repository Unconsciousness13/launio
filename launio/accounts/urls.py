from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy

from launio.accounts.views import UserRegisterView, UserLoginView, ProfilePageView, profile_edit, DeleteProfileView

urlpatterns = (
    path('register/', UserRegisterView.as_view(), name='register page'),
    path('login/', UserLoginView.as_view(), name='login page'),
    path('logout/', auth_views.LogoutView.as_view(next_page=reverse_lazy('show index')), name='logout'),

    path('profile/<int:pk>/', ProfilePageView.as_view(), name='profile view'),
    path('profile-edit/<int:pk>/', profile_edit, name='profile edit'),
    path('profile-delete/<int:pk>', DeleteProfileView.as_view(), name="profile delete"),

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='profile/password-reset.html'),
         name="password_reset"),

    path('password_reset_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name='profile/password-reset-sent.html'),
         name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='profile/password-reset-form.html'),
         name="password_reset_confirm"),

    path('password_reset_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='profile/password-reset-complete.html'),
         name="password_reset_complete"),

)

