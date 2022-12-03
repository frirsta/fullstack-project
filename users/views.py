from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .forms import SignUpForm
from django.contrib import messages


def signup(request):
    if request.user.is_authenticated:
        return redirect('magazine:home')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            messages.success(request, "You are now a registered user!")
            return redirect("magazine:home")
    else:
        form = SignUpForm()
    return render(request, "users/signup.html", {"form": form})
