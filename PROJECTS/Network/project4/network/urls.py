from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),

    path("api/posts", views.get_all_posts,
         name="get_all_posts"),

    path("api/posts/<str:username>", views.get_own_posts,
         name="get_own_posts"),

    path("api/post/<int:post_id>", views.get_post,
         name="get_post"),

    path("api/follow/<str:username>", views.get_following_posts,
         name="get_following"),

    path("api/liked/<str:username>", views.get_liked_post,
         name="get_liked"),

    path("api/new", views.create_new_post,
         name="create_post"),

    path("api/likes/<int:post_id>", views.change_likes,
         name="change_likes"),

    path("api/delete_post/<int:post_id>", views.delete_post,
         name="delete_post"),
]
