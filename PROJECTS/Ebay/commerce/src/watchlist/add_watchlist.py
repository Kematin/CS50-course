from .watchlist import Watchlist, DefaultArguments
from ..exceptions import WatchlistError

class AddToWatchlist(Watchlist):
    def __init__(self, default_arguments: DefaultArguments, WatchlistModel, UserModel):
        super().__init__(default_arguments)
        self.WatchlistModel = WatchlistModel
        self.UserModel = UserModel
        
    def add_to_watchlist(self) -> None:
        username = self.request.user
        user = self.UserModel.objects.get(username=username)
        listing = self.ListingModel.objects.get(id=self.listing_id)

        if self.check_existance(listing, user):
            raise WatchlistError
        else:
            watchlist = self.WatchlistModel(user=user, listing=listing)
            watchlist.save()

    def check_existance(self, listing, user) -> bool:
        exists = self.WatchlistModel.objects.filter(user=user, listing=listing).exists()
        if exists:
            return True
        else:
            return False
