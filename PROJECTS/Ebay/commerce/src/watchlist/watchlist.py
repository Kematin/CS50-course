from django.db import models
from django.http import HttpRequest

from typing import NamedTuple


class DefaultArguments(NamedTuple):
    request: HttpRequest
    listing_id: int
    ListingModel: models.Model


class Watchlist:
    def __init__(self, default_arguments: DefaultArguments):
        self.request, self.listing_id, self.ListingModel = default_arguments
        self.all_listings = self.ListingModel.objects.all()


def add_to_watchlist(default_arguments: DefaultArguments, WatchlistModel, UserModel):
    from .add_watchlist import AddToWatchlist
    logic = AddToWatchlist(default_arguments, WatchlistModel, UserModel)
    logic.add_to_watchlist()

def remove_watchlist(default_arguments: DefaultArguments, WatchlistModel, UserModel):
    from .remove_watchlist import RemoveWatchlist
    logic = RemoveWatchlist(default_arguments, WatchlistModel, UserModel)
    logic.remove_watchlist()

def check_watchlist(default_arguments: DefaultArguments, WatchlistModel, UserModel) -> bool:
    from .check_watchlist import CheckWatchlist
    logic = CheckWatchlist(default_arguments, WatchlistModel, UserModel)
    return logic.check_watchlist()


functions = {
        "add": add_to_watchlist,
        "remove": remove_watchlist,
        "check": check_watchlist,
    }
