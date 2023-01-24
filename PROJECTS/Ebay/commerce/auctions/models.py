from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Category(models.Model):
    name = models.CharField(max_length=25)
    
    def __str__(self):
        return self.name


class Listing(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=500)
    cost = models.FloatField()

    image_url = models.CharField(max_length=100, blank=True)
    user_winner = models.CharField(max_length=150, blank=True)
    category_names = models.ManyToManyField(Category, blank=True, related_name="category")

    def __str__(self):
        return f"{self.name}: price - {self.cost}"
    

class Commentary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commentary_user")
    commentary = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.user}: {self.commentary}"
