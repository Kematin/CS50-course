from django.urls import path

from . import views

urlpatterns = [
    # Main Page
    path("", views.index, name="index"),

    # Listings Page
    path("listing/<int:listing_id>", views.listing, name="listing"),
    path("inactive/<int:listing_id>", views.inactive_listing, name="inactive_listing"),

    # User not login
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("category", views.category, name="category"),
    path("inactive", views.inactive, name="inactive"),

    # User login
    path("watchlist", views.watchlist, name="watchlist"),
    path("won", views.won_listing, name="won"),
    path("create", views.create_listing, name="create"),

    # Error handlers

]
