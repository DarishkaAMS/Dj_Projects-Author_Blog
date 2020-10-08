from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "user.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("indeX"))
        else:
            return render(request, "login.html", {
                "message": "Invalid credentials"
            })
    else:
        return render(request, "login.html")

def logout_view(request):
    logout(request)
    return render(request, "login.html", {
        "message": "Logged out."
    })