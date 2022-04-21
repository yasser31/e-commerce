from django.shortcuts import render
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

