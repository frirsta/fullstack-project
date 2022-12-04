from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email")


class LoginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField()


class AboutMeForm(forms.Form):
    username = forms.CharField()
    about_me = forms.CharField(widget=forms.TextArea())
    image = forms.ImageFields(required=False)
