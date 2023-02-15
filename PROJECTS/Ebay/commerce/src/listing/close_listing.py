from .listing import Listing

class ListingClose(Listing):
    def __init__(self, request, ListingModel):
        super().__init__(request, ListingModel)
 
    def delete_listing(self, listing_id: int) -> bool:
        listing = self.all_listings.get(id=listing_id)
        winner = listing.temporary_winner
        if winner:
            listing.winner = winner
            listing.save()
            return True
        else:
            return False


