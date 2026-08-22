from django.urls import path

from core.views.school import SchoolDetailView, SchoolUpdateView

urlpatterns = [
    path("school/", SchoolDetailView.as_view(), name="school"),
    path("school/update/", SchoolUpdateView.as_view(), name="school_update"),
]
