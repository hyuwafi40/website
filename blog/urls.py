from django.urls import path

from blog.views import (
    AlbumDetailView,
    AlbumListView,
    ArticleDetailView,
    ArticleListView,
    CategoryDetailView,
    CategoryListView,
    IndexView,
    PageDetailView,
    PageListView,
    SearchView,
    CommentCreateView,
)

app_name = "blog"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("articles/", ArticleListView.as_view(), name="article_list"),
    path("articles/<slug:slug>/", ArticleDetailView.as_view(), name="article_detail"),
    path("pages/", PageListView.as_view(), name="page_list"),
    path("pages/<slug:slug>/", PageDetailView.as_view(), name="page_detail"),
    path("categories/", CategoryListView.as_view(), name="category_list"),
    path(
        "categories/<slug:slug>/", CategoryDetailView.as_view(), name="category_detail"
    ),
    path("search/", SearchView.as_view(), name="search"),
    path("albums/", AlbumListView.as_view(), name="album_list"),
    path("albums/<slug:slug>/", AlbumDetailView.as_view(), name="album_detail"),
    path(
        "comments/create/<slug:article_slug>/",
        CommentCreateView.as_view(),
        name="comment_create",
    ),
]
