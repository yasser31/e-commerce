from django.urls import path
from. import views
from django.contrib.auth import views as auth_views

app_name = "users"

urlpatterns = [
   
    path('', views.users, name="users"),
    path("accounts/login/", views.RegistrationView.login_user, name='login'),
    path("accounts/registration", views.RegistrationView.as_view(), name="registration"),
    path("accounts/logout/", auth_views.LogoutView.as_view(), name="logout"),
    path('accounts/activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',  
        views.RegistrationView.activate, name='activate')
    ]