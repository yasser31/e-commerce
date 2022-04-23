from django import forms
from .models import User
from ecom.settings import EMAIL_HOST_USER
from django.core.mail import send_mail


class UserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ["username", "email", "password", "phone", "address"]
        errors = "there is an error"


    def new_user(self):
        username = self.cleaned_data["username"]
        email = self.cleaned_data["email"]
        password = self.cleaned_data["password"]
        phone = self.cleaned_data["phone"]
        address = self.cleaned_data["address"]
        user = User.objects.create_user(username, email, password)
        user.phone = phone
        user.address = address
        user.save()
    
    def send_email_confirmation(self):
        confirmation_link = None
        username = self.cleaned_data["username"]
        email = self.cleaned_data["email"]
        message = f"""Hello {username}, Thank you for joining our website.

                  We would like to confirm that your account was created successfully. 
                  To access [customer portal] click the link below.
                  {confirmation_link}
                  If you experience any issues logging into your account, reach out to us at {EMAIL_HOST_USER}.
                  Best regards
                  The [customer portal] team
        """
        send_mail(
            subject="Account registration confirmation",
            message=message,
            from_email=EMAIL_HOST_USER,
            recipient_list=[email]
        )

class LoginForm(forms.Form):
    username = forms.CharField(label="username", max_length=256, required=True)
    email = forms.EmailField(label="email", max_length=256, required=True)
    password = forms.CharField(widget=forms.PasswordInput)