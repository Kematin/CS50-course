# from .config import ApiException


def create_post(request) -> None:
    data = request.body
    username = request.user
    print(data, username)
