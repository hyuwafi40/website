from django.urls import path

from core.views.resources import BackupView, ResetView, ResourcesView, RestoreView

urlpatterns = [
    path("resources/", ResourcesView.as_view(), name="resources"),
    path("resources/backup/", BackupView.as_view(), name="resources_backup"),
    path("resources/restore/", RestoreView.as_view(), name="resources_restore"),
    path("resources/reset/", ResetView.as_view(), name="resources_reset"),
]
