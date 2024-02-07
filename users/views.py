from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserLoginForm  # You need to create this form
from django.contrib.auth import authenticate, login as auth_login  # Renamed to avoid conflict


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("users/pages/index.html")
    # if the form is not valid, we will render the form again with the error messages
    else:
        form = CustomUserCreationForm()

    return render(request, "users/pages/register.html", {"form": form})

def user_login(request): 
    if request.method == "POST":
        form = CustomUserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)  
                # Redirect to a named route instead of a template
                return redirect("users/pages/index.html") 
    else:
        form = CustomUserLoginForm()
    return render(request, "users/pages/login.html", {"form": form})
