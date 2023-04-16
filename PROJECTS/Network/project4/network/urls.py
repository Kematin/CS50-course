
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),

    path("api/posts", views.get_all_posts_api, name="get_all_posts"),
    path("api/post/<int:post_id>", views.get_post_api, name="get_post"),
]
