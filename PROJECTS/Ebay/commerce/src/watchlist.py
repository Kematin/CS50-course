class Watchlist:
    def __init__(self, request, model):
        self.request = request
        self.model = model
        
    def add_to_watchlist(self, listing_id: int, ListingModel, UserModel) -> bool:
        username = self.request.user
        user = UserModel.objects.get(username=username)
        listing = ListingModel.objects.get(id=listing_id)

        if self.check_existance(listing, user):
            return False
        else:
            watchlist = self.model(user=user, listing=listing)
            watchlist.save()
            return True

    def check_existance(self, listing, user) -> bool:
        exists = self.model.objects.filter(user=user, listing=listing).exists()
        if exists:
            return True
        else:
            return False
