from django.shortcuts import render, HttpResponseRedirect, reverse
from .models import User

# Additional imports we'll need:
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    # If no user is signed in, return to login page:
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "users/index.html")

def login_view(request):
    if request.method == "POST":
        # Accesing username and password
        username = request.POST["username"]
        password = request.POST["password"]

        # Check is username and password are correct
        user = authenticate(request, username=username, password=password)

        print(user)

        # If returned object user will login
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        # Another way - return login page with error message
        else:
            message = "Invalid data"
            return render(request, "users/login.html", {"message": message})
    
    return render(request, "users/login.html")

def logout_view(request):
    ...
