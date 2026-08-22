from django.urls import path

from core.views.album import (
    AlbumCreateView,
    AlbumDeleteView,
    AlbumDetailView,
    AlbumListView,
    AlbumToggleStatusView,
    AlbumUpdateView,
    PhotoCreateView,
    PhotoDeleteView,
    PhotoListView,
)

urlpatterns = [
    path("album/", AlbumListView.as_view(), name="album_list"),
    path("album/create/", AlbumCreateView.as_view(), name="album_create"),
    path("album/<slug:slug>/edit/", AlbumUpdateView.as_view(), name="album_edit"),
    path("album/<slug:slug>/delete/", AlbumDeleteView.as_view(), name="album_delete"),
    path("album/<slug:slug>/toggle/", AlbumToggleStatusView.as_view(), name="album_toggle"),
    path("album/<slug:slug>/", AlbumDetailView.as_view(), name="album_gallery"),
    path("album/<slug:slug>/photo/create/", PhotoCreateView.as_view(), name="photo_create"),
    path("photo/<slug:slug>/delete/", PhotoDeleteView.as_view(), name="photo_delete"),
    path("photos/", PhotoListView.as_view(), name="photo_list"),
]
