from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tom', views.tom, name='tom'),
    path('<str:name>', views.greet, name='greet'),
]
