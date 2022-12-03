from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate

from .forms import SignUpForm, LoginForm
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


def loginUser(request):
    if request.user.is_authenticated:
        return redirect("magazine:home")
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect("magazine:home")
            else:
                messages.error(request, 'Invalid email or password')
    else:
        form = LoginForm()

    return render(request, "users/login.html", {"form": form})
