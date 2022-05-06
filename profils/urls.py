from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from. import views

app_name = "profils"

urlpatterns = [

    path("edit/user-infromation",
         views.UserEditView.as_view(), name="edit_user_information"),
    path("edit/profil-photo",
         views.ProfilPhotoEditView.as_view(), name="edit_profil_photo"),
    path("edit/profil-infromation",
         views.ProfilEditView.as_view(), name="edit_user_information"),
    path("accounts/password_change",
         auth_views.PasswordChangeView.as_view(template_name="profils/password_change.html", 
         success_url=reverse_lazy("profils:password_change_complete")), name="password_change'"),
    path("accounts/password_change_done",
         auth_views.PasswordChangeDoneView.as_view(
         template_name="password_change_complete.html"),
         name="password_change_done'"),
]
