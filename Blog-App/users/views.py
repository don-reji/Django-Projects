from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import LoginForm, RegisterForm


# Create your views here.
def sign_in(request):
    if request.method == "GET":
        # if user already logged in and trying to login
        if request.user.is_authenticated:
            return redirect("post")
        form = LoginForm()
        return render(request, "users/login.html", {"form": form})

    elif (request.method) == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            # cleaned_data is a dictionary cleaned data of containing field names of form,
            # only available if .is_valid() is true
            user = authenticate(request, username=username, password=password)
            # authenticating the user with the same username and password
            if user:
                login(request, user)
                # logining the user
                messages.success(request, f"Hello {username.title()}, welcome.")
                return redirect("posts")
        # if authentication is failed or form not valid
        messages.error(request, "Invalid username or password")
        return render(request, "users/login.html", {"form": form})


def sign_out(request):
    logout(request)
    messages.success(request, "You have been signed out.")
    return redirect("login")


def sign_up(request):
    if request.method == "GET":
        form = RegisterForm()
        return render(request, "users/register.html", {"form": form})

    elif request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            # user = form.save(commit="False")
            # user.username = user.username.lower()
            user=form.save()
            messages.success(request, "You have been registered")
            login(request, user)
            return redirect("posts")
        else:
            return render(request, "users/register.html", {"form": form})
