from .watchlist import Watchlist, DefaultArguments
from ..exceptions import WatchlistError

class RemoveWatchlist(Watchlist):
    def __init__(self, default_arguments: DefaultArguments, WatchlistModel, UserModel):
        super().__init__(default_arguments)
        self.WatchlistModel = WatchlistModel
        self.UserModel = UserModel

    def remove_watchlist(self) -> None:
        listing = self.all_listings.get(id=self.listing_id)
        username = self.request.user
        user = self.UserModel.objects.get(username=username)
        watchlist = self.WatchlistModel.objects.get(user=user, listing=listing)
        watchlist.delete()
