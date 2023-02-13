class Watchlist:
    def __init__(self, request, model):
        self.request = request,
        self.model = model

    def add_to_watchlist(self, listing_id: int, ListingModel, UserModel):
        user = UserModel.objects.get(username=self.request.user)
        listing = ListingModel.objects.get(id=listing_id)
        watchlist = self.model(user=user, listing=listing)
        watchlist.save()
