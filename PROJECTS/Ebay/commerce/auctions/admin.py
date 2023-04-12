from django.contrib import admin
from .models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "password")

class ListingAdmin(admin.ModelAdmin):
    list_display = ("name", "cost", "winner")

class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("user", "commentary")

class WatchlistAdmin(admin.ModelAdmin):
    list_display = ("user", "listing")

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Listing, ListingAdmin)
admin.site.register(Commentary, CommentaryAdmin)
admin.site.register(Watchlist, WatchlistAdmin)
admin.site.register(Category)
