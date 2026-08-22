from django.urls import path

from core.views.account import (
    AccountCreateView,
    AccountDeleteView,
    AccountListView,
    AccountUpdateView,
)

urlpatterns = [
    path("account/", AccountListView.as_view(), name="account_list"),
    path("account/create/", AccountCreateView.as_view(), name="account_create"),
    path("account/<slug:slug>/edit/", AccountUpdateView.as_view(), name="account_edit"),
    path("account/<slug:slug>/delete/", AccountDeleteView.as_view(), name="account_delete"),
]
