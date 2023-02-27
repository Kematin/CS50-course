from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponseRedirect, HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse

from dataclasses import dataclass

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
CommentaryForm
'''

from src import main
listing_functions = main.listing_functions
watchlist_functions = main.watchlist_functions
'''
Listing fucntions: create, upp_cost, close, get_info
Watchlist functions: add, remove, check
Commentary
Watchlist
'''

from src.exceptions import *
'''
ListingError
WatchlistError
'''

@dataclass
class CreateListingArguments:
    data: dict
    request: HttpRequest
    ListingModel: models.Model
    CategoryModel: models.Model

# ------------------------------- MAIN PAGE ------------------------------------


def index(request):
    inactive_listings = Listing.objects.exclude(winner="")
    listings = list(filter(lambda listing: listing not in inactive_listings, Listing.objects.all()))
    context = {"listings": listings}
    return render(request, "auctions/index.html", context)


def listing(request, listing_id):
    # Get all data about listing
    listing = Listing.objects.all().get(id=listing_id)
    categories = listing.category_names.all()
    context = {"listing": listing, "categories": categories}

    # commentaries
    commentaries = Commentary.objects.filter(listing=listing)
    context["commentaries"] = commentaries

    # check creator user
    if listing.creator == request.user:
            context["user_creator"] = "True"

    # commentaries form
    form = CommentaryForm
    context["form"] = form

    # check that listing in watchlist
    default_arguments = (request, listing_id, Listing) 
    if watchlist_functions["check"](default_arguments, Watchlist, User):
        context["watchlist"] = "True"

    return render(request, "auctions/listing.html", context)


def close_listing(request, listing_id):
    if request.method == "POST":
        try:
            default_arguments = (request, listing_id, Listing) 
            listing_functions["close"](default_arguments)
        except ListingError:
            messages.error(request, "Error: Nobody won this listing.")
            return redirect(f"../{listing_id}")

    return redirect(f"inactive")


# ! add feature to display error
def upp_cost_listing(request, listing_id):
    if request.method == "POST":
        try:
            new_cost = float(request.POST["new_cost"])
            default_arguments = (request, listing_id, Listing) 
            listing_functions["upp_cost"](default_arguments, new_cost, User)
        except ListingError:
            messages.error(request, "Error: The new price is less than or equal to the old price.")

    return redirect(f"../{listing_id}")


def add_commentaries(request, listing_id):
    if request.method == "POST":
        form = CommentaryForm(request.POST)
        if form.is_valid():
            commentary = request.POST["commentary"]
            add = main.Commentary(request, Commentary)
            add.add_commentary(commentary, listing_id, User, Listing)

    return redirect(f"../{listing_id}")


def delete_commentaries(request, listing_id, commentary_id):
    if request.method == "POST":
        commentary = Commentary.objects.get(id=commentary_id)
        commentary.delete()

    return redirect(f"../../{listing_id}")


def add_to_watchlist(request, listing_id):
    if request.method == "POST":
        try:
            default_arguments = (request, listing_id, Listing) 
            watchlist_functions["add"](default_arguments, Watchlist, User)
        except WatchlistError:
            messages.error(request, "Error: This listing already in your watchlist.")
            return redirect(f"../{listing_id}")

    return redirect(f"watchlist")


def remove_watchlist(request, listing_id):
    if request.method == "POST":
        try:
            default_arguments = (request, listing_id, Listing) 
            watchlist_functions["remove"](default_arguments, Watchlist, User)
        except WatchlistError:
            messages.error(request, "Error: Cannot remove")
            return redirect(f"../{listing_id}")

    return redirect(f"watchlist")


# ------------------------------- USER LOGIN ------------------------------------


@login_required
def watchlist(request):
    user = User.objects.all().get(username=request.user)
    listings = Watchlist.objects.filter(user=user)
    listings = [listing.listing for listing in listings]
    context = {
            "listings": listings,
        }
    return render(request, "auctions/user_login/watchlist.html", context)


@login_required
def won_listing(request):
    all_listings = Listing.objects.all()
    listings = all_listings.filter(winner=request.user)
    context = {"listings": listings}
    return render(request, "auctions/user_login/won_listing.html", context)


@login_required
def create_listing(request):
    form = ListingForm()

    context = {
        "form": form
    }

    if request.method == "POST":
        form = ListingForm(request.POST)
        if form.is_valid():
            try:
                data = request.POST
                arguments = CreateListingArguments(
                        request=request, ListingModel=Listing, data=data, CategoryModel=Category) 
                listing_functions["create"](arguments)
            except ListingError:
                # ! add feature to display error
                print("error")

            return redirect("index")
        
    if request.method == "GET":
        return render(request, "auctions/user_login/create_listing.html", context)


# ------------------------------- USER NOT LOGIN ------------------------------------


def category(request):
    all_categories = Category.objects.all()
    categories = list()
    for category in all_categories:
        all_listings = Listing.objects.all()
        listings_category = all_listings.filter(category_names=category.id)
        categories.append({category.name: [listings_category]})

    for category_dict in categories:
        print(category_dict)

    context = {"categories": categories}

    return render(request, "auctions/user_not_login/category.html", context)


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
