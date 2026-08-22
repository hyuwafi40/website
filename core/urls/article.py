from django.urls import path

from core.views.article import (
    ArticleCreateView,
    ArticleDeleteView,
    ArticleListView,
    ArticleToggleStatusView,
    ArticleUpdateView,
)

urlpatterns = [
    path("article/", ArticleListView.as_view(), name="article_list"),
    path("article/create/", ArticleCreateView.as_view(), name="article_create"),
    path("article/<slug:slug>/edit/", ArticleUpdateView.as_view(), name="article_edit"),
    path("article/<slug:slug>/delete/", ArticleDeleteView.as_view(), name="article_delete"),
    path("article/<slug:slug>/toggle/", ArticleToggleStatusView.as_view(), name="article_toggle"),
]
