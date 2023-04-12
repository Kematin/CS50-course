from django.contrib.auth.models import AbstractUser
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=25)
    
    def __str__(self):
        return self.name


class User(AbstractUser):
    pass


class Listing(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=500)
    cost = models.FloatField()

    image_url = models.URLField(blank=True)
    category_names = models.ManyToManyField(Category, blank=True, related_name="category")

    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="creator")
    winner = models.CharField(max_length=150, blank=True)
    temporary_winner = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return f"{self.name}: price - {self.cost}"


class Watchlist(models.Model):
    a = models.CharField(max_length=500, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="watchlist_user")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="watchlist")


class Commentary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commentary_user")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="commentary_listing")
    commentary = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.user}: {self.commentary} ({self.listing})"
