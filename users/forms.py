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
    about_me = forms.CharField(widget=forms.Textarea())
    image = forms.ImageField(required=False)

    def __init__(self, og_username, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.og_username = og_username

    def clean_username(self):
        """
        Throws exception if username is taken.
        """

        username = self.cleaned_data['username']
        if username != self.og_username:
            if User.objects.filter(username=username).exists():
                raise forms.ValidationError(
                    'Username already exists.')
        return username
