from network.models import Post, Comment
from typing import TypedDict
from datetime import datetime


class PostJson(TypedDict):
    creator: str
    content: str
    likes: int
    datetime: str
    comments: list[str]


def return_all_posts_json() -> dict[PostJson]:
    all_posts = Post.objects.all()
    all_posts_json = iterate_at_posts_array(all_posts)
    return all_posts_json


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
