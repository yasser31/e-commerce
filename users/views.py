from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.views.generic.edit import FormView
from .forms import UserForm


def users(request):
    return render(request, "users/users.html")

class RegistrationFormView(FormView):
    template_name = 'users/registration/registration.html'
    form_class = UserForm
    success_url = ''
    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.new_user()
        return super().form_valid(form)


def login_user(request):
    error = None
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse("store:store"))
        else:
            error = "Username or Password not correct"
    return render(request, "store/base.html", {"error" : error})       