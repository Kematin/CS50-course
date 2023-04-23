from network.models import User, Post

import json
from datetime import datetime
from .config import PostJson, ApiException


def create_post(request) -> None:
    data = change_data_to_template(request)
    if not check_content_exist(data["content"]):
        raise ApiException("No content for post.")
    else:
        add_post_to_model(data)


def check_content_exist(content: str | None) -> bool:
    if content is None:
        return False
    elif content.strip() == "":
        return False
    else:
        return True


def change_data_to_template(request) -> PostJson:
    data = json.loads(request.body)
    data["creator"] = User.objects.get(username=request.user)
    data["likes"] = 0
    data["datetime"] = datetime.now()
    return data


def add_post_to_model(data: PostJson) -> None:
    Post.objects.create(creator=data["creator"], content=data["content"],
                        likes=data["likes"], datetime=data["datetime"])
