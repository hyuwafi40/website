from django.urls import path

from core.views.tag import (
    TagCreateView,
    TagDeleteView,
    TagListView,
    TagUpdateView,
)

urlpatterns = [
    path("tag/", TagListView.as_view(), name="tag_list"),
    path("tag/create/", TagCreateView.as_view(), name="tag_create"),
    path("tag/<slug:slug>/edit/", TagUpdateView.as_view(), name="tag_edit"),
    path("tag/<slug:slug>/delete/", TagDeleteView.as_view(), name="tag_delete"),
]
