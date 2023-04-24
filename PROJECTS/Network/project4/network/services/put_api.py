from django.core.exceptions import ObjectDoesNotExist

from network.models import Post

from .config import ApiException


def change_likes(request, post_id: int):
    try:
        post = find_post(post_id)
        post.likes += 1
        post.save()
    except ObjectDoesNotExist:
        raise ApiException(f"Post with id {post_id} does not exist")


def find_post(post_id: int) -> Post:
    post = Post.objects.get(id=post_id)
    return post
