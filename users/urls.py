from django.urls import path
from. import views
from django.contrib.auth import views as auth_views

app_name = "users"

urlpatterns = [
   
    path('', views.users, name="users"),
    path("accounts/login/", views.login_user, name='login'),
    path("accounts/registration", views.RegistrationFormView.as_view(), name="registration"),
    path("accounts/logout/", auth_views.LogoutView.as_view(), name="logout")
    ]