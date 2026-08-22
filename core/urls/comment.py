from django.urls import path

from core.views.comment import (
    CommentDeleteView,
    CommentListView,
    CommentUpdateStatusView,
)

urlpatterns = [
    path("comment/", CommentListView.as_view(), name="comment_list"),
    path("comment/<int:pk>/update-status/", CommentUpdateStatusView.as_view(), name="comment_update_status"),
    path("comment/<int:pk>/delete/", CommentDeleteView.as_view(), name="comment_delete"),
]
