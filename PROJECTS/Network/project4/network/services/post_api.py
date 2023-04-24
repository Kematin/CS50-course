from network.models import User, Post

import json
from json.decoder import JSONDecodeError

from datetime import datetime
from .config import PostJson, ApiException


def create_post(request) -> None:
    data = change_data_to_template(request)
    add_post_to_model(data)


def change_data_to_template(request) -> PostJson:
    try:
        print(request.body)
        data = json.loads(request.body)
        data["creator"] = User.objects.get(username=request.user)
        data["likes"] = 0
        data["datetime"] = datetime.now()
        return data
    except JSONDecodeError:
        raise ApiException("No content for post.")


def add_post_to_model(data: PostJson) -> None:
    Post.objects.create(creator=data["creator"], content=data["content"],
                        likes=data["likes"], datetime=data["datetime"])
