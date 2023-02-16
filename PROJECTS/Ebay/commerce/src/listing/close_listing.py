from .listing import Listing, DefaultArguments
from ..exceptions import ListingError

class ListingClose(Listing):
    def __init__(self, default_arguments: DefaultArguments):
        super().__init__(default_arguments)
 
    def delete_listing(self) -> None:
        listing = self.all_listings.get(id=self.listing_id)
        winner = listing.temporary_winner
        if winner:
            listing.winner = winner
            listing.save()
        else:
            raise ListingError


