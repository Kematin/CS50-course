from django.contrib import admin
from .models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "password")

class ListingAdmin(admin.ModelAdmin):
    list_display = ("name", "cost", "user_winner")

class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("user", "commentary")


# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Listing, ListingAdmin)
admin.site.register(Commentary, CommentaryAdmin)
admin.site.register(Category)
