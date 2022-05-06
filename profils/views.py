from django.shortcuts import render
from django.views.generic.edit import UpdateView
from users.models import User
from.models import Profil

class UserEditView(UpdateView):
    
    model = User
    fields = ["username", "email", "phone", "address"]
    template_name = "profils/edit_profil.html"


class ProfilEditView(UpdateView):
    
    model = Profil
    fields = ["description"]
    template_name = None


class ProfilPhotoEditView(UpdateView):
    model = Profil
    fields = ["photo"]