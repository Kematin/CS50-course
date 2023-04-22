from django.contrib.auth import logout
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from network.services import get_api, post_api
from network.services import source_cs50
from network.services.config import ApiException


def index(request):
    if request.user.is_authenticated:
        return render(request, "network/inbox.html")
    else:
        return HttpResponseRedirect(reverse("login"))


# * ------------------------------------------------- API POST


@csrf_exempt
def create_new_post(request):
    if request.method != "POST":
        return JsonResponse(
            {"error": f"{request.method} method is not defined"}, status=400)
    try:
        post_api.create_post(request)
        return JsonResponse({"message": "Succesfull"}, status=200)
    except ApiException as error:
        return JsonResponse({"error": str(error)}, status=400)


# * ------------------------------------------------- API PUT


# TODO data = request.body
def change_likes(request):
    pass


# * ------------------------------------------------- API GET


def get_following_posts(request, username: str):
    try:
        follow_posts = get_api.return_follow_posts_json(username)
        return JsonResponse(follow_posts, status=200)
    except ApiException as error:
        return JsonResponse({"error": str(error)}, status=400)


def get_all_posts(request):
    try:
        all_posts = get_api.return_all_posts_json()
        return JsonResponse(all_posts, status=200)
    except ApiException as error:
        return JsonResponse({"error": str(error)}, status=400)


def get_post(request, post_id: int):
    try:
        post = get_api.return_post_json(post_id)
        return JsonResponse(post, status=200)
    except ApiException as error:
        return JsonResponse({"error": str(error)}, status=400)


def get_own_posts(request, username: str):
    try:
        own_posts = get_api.return_own_posts_json(username)
        return JsonResponse(own_posts, status=200)
    except ApiException as error:
        return JsonResponse({"error": str(error)}, status=400)


# ! ------------------------------------------------- SOURCE CODE


def login_view(request):
    if request.method == "POST":
        return source_cs50.login_view_post(request)
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        return source_cs50.register_post(request)
    else:
        return render(request, "network/register.html")
