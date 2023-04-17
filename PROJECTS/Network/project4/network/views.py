from django.contrib.auth import logout
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse

from network.services import main
from network.services import source_cs50
from network.services.config import ApiException


def index(request):
    return render(request, "network/index.html")


# * ------------------------------------------------- API POST


def create_new_post(request):
    pass


# * ------------------------------------------------- API PUT


def change_likes(request):
    pass


# * ------------------------------------------------- API GET


def get_all_posts(request):
    try:
        all_posts = main.return_all_posts_json()
        return JsonResponse(all_posts, status=200)
    except ApiException as error:
        return JsonResponse({"error": str(error)}, status=400)


def get_post(request, post_id):
    try:
        post = main.return_post(post_id)
        return JsonResponse(post, status=200)
    except ApiException as error:
        return JsonResponse({"error": str(error)}, status=400)


def get_own_posts(request, username):
    try:
        own_posts = main.return_own_posts_json(username)
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
