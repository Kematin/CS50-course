from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import *
'''
Listing
User
Category
Watchlist
Commentary
'''
from .forms import *
'''
ListingForm
'''

from src import main

# ------------------------------- MAIN PAGE ------------------------------------


def index(request):
    inactive_listings = Listing.objects.exclude(winner="")
    listings = list(filter(lambda listing: listing not in inactive_listings, Listing.objects.all()))
    context = {"listings": listings}
    return render(request, "auctions/index.html", context)


def listing(request, listing_id):
    listing = Listing.objects.all().get(id=listing_id)
    categories = listing.category_names.all()
    context = {"listing": listing, "categories": categories}

    if request.method == "POST":
        # Delete listing (go to inactive with winner)
        if listing.creator == request.user:
            delete = main.Listing(request, Listing)
            delete.delete_listing(listing_id, User)

        # Upp cost for listing
        else:
            new_cost = float(request.POST["new_cost"])
            upp = main.Listing(request, Listing)
            result = upp.upp_cost(listing_id, new_cost)
            if result is None:
                context["upp_cost_error"] = "The new price is less than or equal to the old one"
                return render(request, "auctions/listing.html", context)

        return redirect("index")
                        

    if request.method == "GET":
        if listing.creator == request.user:
            context["user_creator"] = "True"
        return render(request, "auctions/listing.html", context)


# ------------------------------- USER LOGIN ------------------------------------


@login_required
def watchlist(request):
    return render(request, "auctions/user_login/watchlist.html")


@login_required
def won_listing(request):
    return render(request, "auctions/user_login/won_listing.html")


@login_required
def create_listing(request):
    form = ListingForm()

    context = {
        "form": form
    }

    if request.method == "POST":
        form = ListingForm(request.POST)
        if form.is_valid():
            data = request.POST
            create = main.Listing(request, Listing)
            result = create.create_listing(data)
            
            if result is None:
                context["message"] = "Listing with same name already exist."
                return render(request, "auctions/user_login/create_listing.html", context)
            else:
                return redirect("index")
        
    if request.method == "GET":
        return render(request, "auctions/user_login/create_listing.html", context)


# ------------------------------- USER NOT LOGIN ------------------------------------


def category(request):
    return render(request, "auctions/user_not_login/category.html")


def inactive(request):
    inactive_listings = Listing.objects.exclude(winner="")
    context = {"listings": inactive_listings}
    return render(request, "auctions/user_not_login/inactive.html", context)

def inactive_listing(request, listing_id):
    listing = Listing.objects.all().get(id=listing_id)
    categories = listing.category_names.all()
    context = {"listing": listing, "categories": categories}
    return render(request, "auctions/inactive_listing.html", context)


# ------------------------------- BY CS50 ------------------------------------


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/user_not_login/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/user_not_login/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/user_not_login/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/user_not_login/register.html")
