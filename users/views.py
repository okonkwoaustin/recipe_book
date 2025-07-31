from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from . forms import UserRegistionForm
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import get_template
from django.template import context


def signup(request):
    if request.method == "POST":
        form = UserRegistionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Your accont has been created ! You can now log in")
            return redirect("login")
    else:
        form = UserRegistionForm()
        return render(request, "users/signup.html", {"form": form})
    
def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username = username, password = password)
            if user is not None:
                form = login(request, user)
                messages.success(request, f"Welcome {username} !!")
                return redirect("index")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
        return render(request, "users/login.html", {"form": form})
    
@login_required 
def settings(request):
    return render(request, "users/settings.html")
