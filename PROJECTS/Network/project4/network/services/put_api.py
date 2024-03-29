from django.core.exceptions import ObjectDoesNotExist

from network.models import Post, Liked, User

from .config import ApiException

import json
from time import sleep


def change_likes(request, post_id: int):
    try:
        isLiked, username = get_username_and_is_liked(request)
        change_like_value(post_id, isLiked, username)
    except ObjectDoesNotExist:
        raise ApiException(f"Post with id {post_id} does not exist")


def change_like_value(post_id: int, isLiked: bool, username: str):
    if isLiked is None or username is None:
        raise ApiException("No value for isLiked or username.")

    user = User.objects.get(username=username)
    liked = Liked.objects.get(user=user)
    liked_posts = liked.liked_post.all()
    liked_posts_id = [post.id for post in liked_posts]

    if isLiked:
        delete_from_liked(liked_posts_id, post_id, liked)
    else:
        add_to_liked(liked_posts_id, post_id, liked)


def delete_from_liked(liked_posts: list, post_id: int, liked: Liked):
    del liked_posts[liked_posts.index(post_id)]
    liked.liked_post.set(liked_posts)
    liked.save()
    sleep(0.3)

    post = Post.objects.get(id=post_id)
    post.likes -= 1
    post.save()
    sleep(0.3)


def add_to_liked(liked_posts: list, post_id: int, liked: Liked):
    liked_posts.append(post_id)
    liked.liked_post.set(liked_posts)
    liked.save()
    sleep(0.3)

    post = Post.objects.get(id=post_id)
    post.likes += 1
    post.save()
    sleep(0.3)


def get_username_and_is_liked(request) -> tuple[bool, str]:
    data = json.loads(request.body)
    is_liked = data.get("isLiked")
    username = data.get("username")
    return is_liked, username


def find_post(post_id: int) -> Post:
    post = Post.objects.get(id=post_id)
    return post
