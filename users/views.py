from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.views.generic.edit import CreateView
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import send_mail
from.models import User
from ecom.settings import EMAIL_HOST_USER
from django.db import transaction



class RegistrationView(CreateView):
    template_name = 'users/registration/registration.html'
    model = User
    fields = ["username", "email", "password", "phone", "address"] 
    success_url = '/'


    @transaction.atomic
    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        response = super().form_valid(form)
        current_site = get_current_site(self.request)
        subject = 'Activate your account.'
        message = render_to_string('users/registration/acc_active_email.html', {
                'user': self.object,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(self.object.pk)),
                'token':account_activation_token.make_token(self.object),
            })
        email = self.object.email
        send_mail(
            subject=subject,
            message=message,
            from_email=EMAIL_HOST_USER,
            recipient_list=[email]
        )
        return response

    def activate(request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and account_activation_token.check_token(user, token):
            user.confirmed = True
            user.save()
            login(request, user)
            return redirect('/')
        else:
            return HttpResponse('Activation link is invalid!')

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