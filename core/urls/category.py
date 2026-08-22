from django.urls import path

from core.views.category import (
    CategoryCreateView,
    CategoryDeleteView,
    CategoryListView,
    CategoryUpdateView,
)

urlpatterns = [
    path("category/", CategoryListView.as_view(), name="category_list"),
    path("category/create/", CategoryCreateView.as_view(), name="category_create"),
    path("category/<slug:slug>/edit/", CategoryUpdateView.as_view(), name="category_edit"),
    path("category/<slug:slug>/delete/", CategoryDeleteView.as_view(), name="category_delete"),
]
