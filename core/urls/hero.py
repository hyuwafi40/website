from django.urls import path

from core.views.hero import (
    HeroCreateView,
    HeroDeleteView,
    HeroListView,
    HeroUpdateView,
)

urlpatterns = [
    path("hero/", HeroListView.as_view(), name="hero_list"),
    path("hero/create/", HeroCreateView.as_view(), name="hero_create"),
    path("hero/<slug:slug>/edit/", HeroUpdateView.as_view(), name="hero_edit"),
    path("hero/<slug:slug>/delete/", HeroDeleteView.as_view(), name="hero_delete"),
]
