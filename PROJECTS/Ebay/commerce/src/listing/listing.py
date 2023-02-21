from django.db import models
from django.http import HttpRequest

from typing import NamedTuple
from dataclasses import dataclass


class DefaultArguments(NamedTuple):
    request: HttpRequest
    listing_id: int
    ListingModel: models.Model


@dataclass
class CreateListingArguments:
    data: dict
    request: HttpRequest
    ListingModel: models.Model
    CategoryModel: models.Model


class Listing:
    def __init__(self, default_arguments: DefaultArguments):
        self.request, self.listing_id, self.ListingModel = default_arguments
        self.all_listings = self.ListingModel.objects.all()


def close_listing(default_arguments: DefaultArguments) -> None:
    from .close_listing import ListingClose
    logic = ListingClose(default_arguments)
    logic.delete_listing()


def upp_cost_listing(default_arguments: DefaultArguments, new_cost: int, UserModel: models.Model) -> None:
    from .upp_cost_listing import ListingUppCost
    logic = ListingUppCost(default_arguments, new_cost, UserModel)
    logic.upp_cost()
    

def create_listing(create_arguments: CreateListingArguments) -> None:
    from .create_listing import ListingCreateNew
    logic = ListingCreateNew(create_arguments)
    logic.create_listing()
   



functions = {
        "close": close_listing,
        "upp_cost": upp_cost_listing,
        "create": create_listing,
    }
