from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.db import models


class User(AbstractUser):
    pass


class Comment(models.Model):
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comment_creator")
    comment = models.CharField(max_length=500)

    def __str__(self) -> str:
        return f"{self.creator}: {self.comment}"


class Post(models.Model):
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="post_creator")
    content = models.TextField(max_length=800)
    likes = models.IntegerField(validators=[MinValueValidator(0)])
    datetime = models.DateTimeField()
    comments = models.ManyToManyField(
        Comment, related_name="post_comments", blank=True)

    def __str__(self) -> str:
        return f"{self.creator}: {self.content}"


class Follow(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_follow")
    following = models.ManyToManyField(
        User, related_name="user_following", blank=True)
    followers = models.ManyToManyField(
        User, related_name="user_followers", blank=True)
    following_posts = models.ManyToManyField(
        Post, related_name="post_following", blank=True)

    def __str__(self) -> str:
        return f"Edit Follow for {self.user}"


class Liked(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_liked")
    liked_post = models.ManyToManyField(
        Post, related_name="post_liked", blank=True)

    def __str__(self) -> str:
        return f"Edit Likes for {self.user}"
