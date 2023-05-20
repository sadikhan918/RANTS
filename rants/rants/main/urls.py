from django.urls import path

from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:id>", views.userPage, name="userPage"),
    path("home/", views.home, name="home"),
    # path("<str:username>", views.userPage, name="userPage")
    # path("makePost/", views.makePost, name="makePost")
]