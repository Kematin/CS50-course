from django.shortcuts import render, HttpResponseRedirect, reverse
from .models import User

# Create your views here.
def index(request):
    # If no user is signed in, return to login page:
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "users/user.html")


def login_view(request):
    if request.method == "POST":
        # Accessing username and password from form data
        username = request.POST["username"]
        password = request.POST["password"]

        if check_exist_user(username, password):
            return render(request, "users/user.html")
        else:
            message = "Invalid Data"
            return render(request, "users/login.html", {"message": message})

    return render(request, "users/login.html")


def logout_view(request):
    pass


def check_exist_user(username, password):
    try:
        user = User.objects.all().get(login=username)
        if password == user.password:
            return True
        else:
            return False

    except Exception as e:
        print(e)
        return False
