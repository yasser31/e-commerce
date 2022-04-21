from django import forms
from .models import User


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


class LoginForm(forms.Form):
    username = forms.CharField(label="username", max_length=256, required=True)
    email = forms.EmailField(label="email", max_length=256, required=True)
    password = forms.CharField(widget=forms.PasswordInput)