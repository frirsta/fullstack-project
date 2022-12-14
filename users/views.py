from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse
from .models import User, Profile
from .forms import SignUpForm, LoginForm, AboutMeForm
from django.contrib import messages


def signup(request):
    """
    This function handles the signup form.
    This function creates a User instance.
    The user is logged in with the login() funtion.
    When user is created they get redirected to home.html.

    """
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
    """
    This functions handles the login form.
    When they user logs in they get redirected to home.html.
    This function dispays a message on the page if the username or password is incorrect.
    """
    if request.user.is_authenticated:
        return redirect("magazine:home")
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect("magazine:home")
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = LoginForm()

    return render(request, "users/login.html", {"form": form})


def logoutUser(request):
    """
    This function redirects the user to login page when the user logs out.
    """
    logout(request)
    return redirect(reverse("users:login"))


@login_required
def profile(request, username):
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, user=user)
    return render(request, 'users/profile.html', {'profile': profile, 'user': user})


@login_required
def edit_user_profile(request):
    if request.method == 'POST':
        form = AboutMeForm(request.user.username, request.POST, request.FILES)
        if form.is_valid():
            about_me = form.cleaned_data["about_me"]
            username = form.cleaned_data["username"]
            image = form.cleaned_data["image"]

            user = User.objects.get(id=request.user.id)
            profile = Profile.objects.get(user=user)
            user.username = username
            user.save()
            profile.about_me = about_me
            if image:
                profile.image = image
            profile.save()
            return redirect("users:profile", username=user.username)
    else:
        form = AboutMeForm(request.user.username)
    return render(request, "users/about_user.html", {"form": form})
