from django.core.exceptions import ObjectDoesNotExist

from network.models import Post, Comment
from datetime import datetime

from .config import ApiException, PostJson


def return_all_posts_json() -> dict[PostJson]:
    all_posts = Post.objects.all()
    if len(all_posts) == 0:
        raise ApiException("No posts")
    else:
        all_posts_json = iterate_at_posts_array(all_posts)
        return all_posts_json


def return_post(post_id: int) -> PostJson:
    try:
        post = Post.objects.get(id=post_id)
        post_json = create_post_json(post)
        return post_json
    except ObjectDoesNotExist:
        raise ApiException(f"Post with id {post_id} does not exist")


def iterate_at_posts_array(posts_array: list[Post]) -> dict[PostJson]:
    posts_array_json = {}
    for post in posts_array:
        post_json = create_post_json(post)
        posts_array_json[post.id] = post_json

    return posts_array_json


def create_post_json(post: Post) -> PostJson:
    comments = get_comments_from_objects(post.comments.all())
    datetime = format_time(post.datetime)
    post_json = PostJson(
                            creator=post.creator.username,
                            content=post.content,
                            likes=post.likes,
                            datetime=datetime,
                            comments=comments
                        )

    return post_json


def get_comments_from_objects(comments: list[Comment]) -> list[str]:
    new_comments = [comment.comment for comment in comments]
    return new_comments


def format_time(time: datetime):
    formatted_time = time.strftime('%B %d, %Y, %I:%M %p')
    return formatted_time
