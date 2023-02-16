from .listing import Listing, DefaultArguments
from ..exceptions import ListingError

class ListingUppCost(Listing):
    def __init__(self, default_arguments: DefaultArguments, new_cost: int, UserModel):
        super().__init__(default_arguments)
        self.new_cost = new_cost
        self.UserModel = UserModel

    # Return False if new cost less than old
    def upp_cost(self) -> None:
        listing = self.all_listings.get(id=self.listing_id)
        old_cost = listing.cost

        if self.check_new_cost(old_cost, self.new_cost):
            raise ListingError
        else:
            temporary_winner = self.UserModel.objects.get(username=self.request.user)
            listing.cost = self.new_cost
            listing.temporary_winner = temporary_winner.username
            listing.save()

    def check_new_cost(self, old_cost, new_cost) -> bool:
        if new_cost <= old_cost:
            return True
        else:
            return False
