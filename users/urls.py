from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy
from. import views


app_name = "users"

urlpatterns = [

    path("accounts/login/", views.RegistrationView.login_user, name='login'),
    path("accounts/registration",
         views.RegistrationView.as_view(), name="registration"),
    path("accounts/logout/", auth_views.LogoutView.as_view(), name="logout"),
    path('accounts/activate/<uidb64>/(<token>/',
         views.RegistrationView.activate, name='activate'),
    path(
        'accounts/reset-password/',
        auth_views.PasswordResetView.as_view(
            template_name='users/registration/reset-password.html',
            success_url=reverse_lazy("users:password_reset_done")),  name='reset_password'),
    path("accounts/password_reset/done/",
         auth_views.PasswordResetDoneView.as_view(
             template_name="users/registration/password_reset_done.html"),
         name="password_reset_done"),
    path("accounts/password_reset_confirm/<uidb64>/(<token>",
         auth_views.PasswordResetConfirmView.as_view(
             template_name="users/registration/password_reset_confirm.html",
             success_url=reverse_lazy("users:password_reset_complete")),
         name="password_reset_confirm"),
    path("accounts/password_reset_complete",
         auth_views.PasswordResetCompleteView.as_view(
             template_name="users/registration/password_reset_complete.html"),
         name="password_reset_complete"),
]
