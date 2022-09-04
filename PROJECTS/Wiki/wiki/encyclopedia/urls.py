from django.urls import path

from . import views
from . import util
list_entries = util.list_entries()

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:article>", views.open_article_page, name="article"),
    path("wiki/", views.index, name="wiki"),
]
