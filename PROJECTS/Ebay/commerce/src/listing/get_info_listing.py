from .listing import Listing

class ListingGetInfo(Listing):
    def __init__(self, request, ListingModel):
        super().__init__(request, ListingModel)
