from django.urls import path

from core.views.brand import BrandDetailView, BrandUpdateView

urlpatterns = [
    path("brand/", BrandDetailView.as_view(), name="brand"),
    path("brand/update/", BrandUpdateView.as_view(), name="brand_update"),
]
