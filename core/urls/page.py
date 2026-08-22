from django.urls import path

from core.views.page import (
    PageCreateView,
    PageDeleteView,
    PageListView,
    PageUpdateView,
)

urlpatterns = [
    path("page/", PageListView.as_view(), name="page_list"),
    path("page/create/", PageCreateView.as_view(), name="page_create"),
    path("page/<slug:slug>/edit/", PageUpdateView.as_view(), name="page_edit"),
    path("page/<slug:slug>/delete/", PageDeleteView.as_view(), name="page_delete"),
]
