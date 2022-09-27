from django.urls import path
from . import views

urlpatterns = [
    path("", views.indexPage, name="indexPage"),
    path("blogs", views.blogsPage, name="blogsPage"),
    path("blogs/<slug:slug>", views.blogDetailPage, name="blogDetailPage"),
]