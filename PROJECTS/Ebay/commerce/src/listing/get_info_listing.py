from .listing import Listing

class ListingGetInfo(Listing):
    def __init__(self, request, listing_id, ListingModel):
        super().__init__(request, listing_id, ListingModel)
