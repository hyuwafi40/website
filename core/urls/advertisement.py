from django.urls import path

from core.views.advertisement import (
    AdvertisementCreateView,
    AdvertisementDeleteView,
    AdvertisementListView,
    AdvertisementUpdateView,
)

urlpatterns = [
    path("advertisement/", AdvertisementListView.as_view(), name="advertisement_list"),
    path("advertisement/create/", AdvertisementCreateView.as_view(), name="advertisement_create"),
    path("advertisement/<slug:slug>/edit/", AdvertisementUpdateView.as_view(), name="advertisement_edit"),
    path("advertisement/<slug:slug>/delete/", AdvertisementDeleteView.as_view(), name="advertisement_delete"),
]
