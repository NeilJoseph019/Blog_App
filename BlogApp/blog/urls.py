from django.urls import path
from . import views

urlpatterns = [
    path("", views.indexPage, name="indexPage"),
    path("posts", views.postsPage, name="postsPage"),
    path("posts/<slug:slug>", views.postDetailPage, name="postDetailPage"),
]