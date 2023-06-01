from django.core.exceptions import ObjectDoesNotExist

from network.models import Post

from .config import ApiException


def delete_post(post_id: int):
    try:
        post = Post.objects.get(id=post_id)
        print(post)
        post.delete()
    except ObjectDoesNotExist:
        raise ApiException(f"Post with id {post_id} does not exist")
