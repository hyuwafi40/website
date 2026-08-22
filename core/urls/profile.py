from django.urls import path

from core.views.profile import ProfileDetailView, ProfileUpdateView

urlpatterns = [
    path("profile/", ProfileDetailView.as_view(), name="profile"),
    path("profile/edit/", ProfileUpdateView.as_view(), name="profile_edit"),
]
