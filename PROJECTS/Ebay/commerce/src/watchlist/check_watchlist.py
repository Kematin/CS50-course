from .watchlist import Watchlist, DefaultArguments

class CheckWatchlist(Watchlist):
    def __init__(self, default_arguments: DefaultArguments, WatchlistModel, UserModel):
        super().__init__(default_arguments)
        self.WatchlistModel = WatchlistModel
        self.UserModel = UserModel

    def check_watchlist(self) -> bool:
        listing = self.all_listings.get(id=self.listing_id)
        username = self.request.user
        user = self.UserModel.objects.get(username=username)
        exists = self.WatchlistModel.objects.filter(user=user, listing=listing).exists()
        if exists:
            return True
        else:
            return False
