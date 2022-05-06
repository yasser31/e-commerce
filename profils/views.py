from django.shortcuts import render
from django.views.generic.edit import UpdateView
from users.models import User


class ProfilEditView(UpdateView):
    
    model = User
    fields = ["username", "email", "phone", "address"]
    template_name = "profils/edit_profil.html"


