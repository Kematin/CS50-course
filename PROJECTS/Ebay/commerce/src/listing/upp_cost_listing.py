from .listing import Listing

class ListingUppCost(Listing):
    def __init__(self, request, ListingModel):
        super().__init__(request, ListingModel)

    # Return False if new cost less than old
    def upp_cost(self, listing_id: int, new_cost: float, UserModel) -> bool:
        listing = self.all_listings.get(id=listing_id)
        old_cost = listing.cost

        if self.check_new_cost(old_cost, new_cost):
            return False
        else:
            temporary_winner = UserModel.objects.get(username=self.request.user)
            listing.cost = new_cost
            listing.temporary_winner = temporary_winner.username
            listing.save()
            return True

    def check_new_cost(self, old_cost, new_cost) -> bool:
        if new_cost <= old_cost:
            return True
        else:
            return False
