from django.core.exceptions import ObjectDoesNotExist

from network.models import Post, Comment, User, Follow, Liked
from datetime import datetime

from .config import ApiException, PostJson


def return_all_posts_json() -> dict[PostJson]:
    all_posts = Post.objects.all()
    return check_len_of_post(all_posts, "No posts.")


def return_liked_posts_json(username: str) -> list[int]:
    try:
        user = User.objects.get(username=username)
    except ObjectDoesNotExist:
        raise ApiException(f"User {username} does not exist.")

    try:
        liked = Liked.objects.get(user=user)
        liked_posts = liked.liked_post.all()
        return list(liked_posts)
    except ObjectDoesNotExist:
        Liked.objects.create(user=user)
        return []


def return_follow_posts_json(username: str) -> dict[PostJson]:
    try:
        follow = Follow.objects.get(user=User.objects.get(username=username))
        following_posts = follow.following_posts.all()
        message = f"No following posts for user {username}."
        return check_len_of_post(following_posts, message)
    except ObjectDoesNotExist:
        error_message = f'Object "Follow" for user {username} does not exist.'
        raise ApiException(error_message)


def return_own_posts_json(username: str) -> dict[PostJson]:
    try:
        own_posts = Post.objects.filter(
            creator=User.objects.get(username=username))
        return check_len_of_post(own_posts, f"No posts for user {username}.")
    except ObjectDoesNotExist:
        raise ApiException(f"User {username} does not exist.")


def return_post_json(post_id: int) -> PostJson:
    try:
        post = Post.objects.get(id=post_id)
        post_json = generate_post_json(post)
        return post_json
    except ObjectDoesNotExist:
        raise ApiException(f"Post with id {post_id} does not exist.")


def iterate_at_posts_array(posts_array: list[Post]) -> dict[PostJson]:
    posts_array_json = {}
    for post in posts_array:
        post_json = generate_post_json(post)
        posts_array_json[post.id] = post_json

    return posts_array_json


def generate_post_json(post: Post) -> PostJson:
    comments = get_comments_from_objects(post.comments.all())
    datetime = format_time(post.datetime)
    post_json = PostJson(
        id=post.id,
        creator=post.creator.username,
        content=post.content,
        likes=post.likes,
        datetime=datetime,
        comments=comments,
    )

    return post_json


def check_len_of_post(posts: list[Post], message: str):
    if len(posts) == 0:
        raise ApiException(message)
    else:
        own_posts_json = iterate_at_posts_array(posts)
        return own_posts_json


def get_comments_from_objects(comments: list[Comment]) -> list[dict[str, str]]:
    new_comments = list()
    for comment in comments:
        comment_object = Comment.objects.get(id=comment.id)
        creator = comment_object.creator.username
        comment = comment_object.comment
        new_comments.append({"creator": creator, "comment": comment})

    return new_comments


def format_time(time: datetime):
    formatted_time = time.strftime("%B %d, %Y, %I:%M %p")
    return formatted_time
