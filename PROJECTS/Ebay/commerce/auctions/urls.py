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

    # Additionaly for listing
    path("listing/commentaries/<int:listing_id>", views.add_commentaries, name="add_commentaries"),
    path("listing/close/<int:listing_id>", views.close_listing, name="close_listing"),
    path("listing/upp/<int:listing_id>", views.upp_cost_listing, name="upp_cost"),
    path("listing/watchlist/<int:listing_id>", views.add_to_watchlist, name="add_to_watchlist"),

    # Error handlers

]
