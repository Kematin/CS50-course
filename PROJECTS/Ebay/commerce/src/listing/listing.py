from django.db import models
from django.http import HttpRequest
from ..exceptions import ListingError


class Listing:
    def __init__(self, request: HttpRequest, listing_id: int, ListingModel: models.Model):
        self.ListingModel = ListingModel
        self.request = request
        self.listing_id = listing_id
        self.all_listings = self.ListingModel.objects.all()


def close_listing(request: HttpRequest, listing_id: int, 
                  ListingModel: models.Model):
    pass

def upp_cost_listing(request: HttpRequest, listing_id: int, 
                     ListingModel: models.Model):
    pass

def create_listing(request: HttpRequest, listing_id: int, 
                   ListingModel: models.Model):
    pass

def get_info_about_listing(request: HttpRequest, listing_id: int,
                           ListingModel: models.Model):
    pass


functions = {
        "close": close_listing,
        "upp_cost": upp_cost_listing,
        "create": create_listing,
        "get_info": get_info_about_listing,
    }
