from .watchlist import Watchlist, DefaultArguments
from ..exceptions import WatchlistError

class RemoveWatchlist(Watchlist):
    def __init__(self, default_arguments: DefaultArguments, WatchlistModel, UserModel):
        super().__init__(default_arguments)
        self.WatchlistModel = WatchlistModel
        self.UserModel = UserModel

    def remove_watchlist(self):
        pass
