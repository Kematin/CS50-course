from django.urls import path, re_path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:article>", views.open_article_page, name="article"),
    path("wiki/", views.index, name="wiki"),
    path("add", views.add_new_article, name="add"),
    path("edit/<str:title>", views.edit_article, name="edit"),
    re_path(r"^", views.handler404, name="404"),
]

