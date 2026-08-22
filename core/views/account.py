from django.contrib import messages
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.shortcuts import redirect, render

from core.forms.account import AccountAdminForm
from core.models.user import Account, Profile
from core.utilities.constants import JOB_DEVELOPER
from core.utilities.pagination import paginate
from core.utilities.responses import get_object_or_json
from core.views.base import BaseAccountView


class AccountListView(BaseAccountView):
    template_name = "core/account.html"
    paginate_by = 10

    def get(self, request):
        queryset = (
            Account.objects.exclude(job=JOB_DEVELOPER)
            .select_related("profile")
            .order_by("-date_joined")
        )
        page_obj, page_range = paginate(request, queryset, self.paginate_by)
        for account in page_obj.object_list:
            Profile.objects.get_or_create(account=account)
        form = AccountAdminForm()
        context = {
            "accounts": page_obj.object_list,
            "page_obj": page_obj,
            "page_range": page_range,
            "form": form,
        }
        return render(request, self.template_name, context)


class AccountCreateView(BaseAccountView):
    def post(self, request):
        form = AccountAdminForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data.get("password")
            if not password:
                return self.json_error(
                    "Password wajib diisi saat membuat pengguna.", status=400
                )

            account = form.save(commit=False)
            try:
                validate_password(password, account)
            except ValidationError as e:
                return self.json_error(e.messages, status=400)

            account.set_password(password)
            account.save()

            profile, created = Profile.objects.get_or_create(account=account)
            profile.photo = form.cleaned_data.get("photo") or ""
            profile.gender = form.cleaned_data.get("gender") or ""
            profile.save()

            return self.json_success("Pengguna berhasil dibuat.")
        return self.json_form_error(form)


class AccountUpdateView(BaseAccountView):
    def post(self, request, slug):
        account_or_response = get_object_or_json(Account, slug=slug)
        if isinstance(account_or_response, JsonResponse):
            return account_or_response
        account = account_or_response

        if self.is_developer_account(account):
            return self.json_error(
                "Pengguna Developer tidak dapat diubah melalui halaman ini.",
                status=403,
            )

        form = AccountAdminForm(request.POST, instance=account)
        if form.is_valid():
            password = form.cleaned_data.get("password")
            account = form.save(commit=False)
            if password:
                try:
                    validate_password(password, account)
                except ValidationError as e:
                    return self.json_error(e.messages, status=400)
                account.set_password(password)
            account.save()

            profile, created = Profile.objects.get_or_create(account=account)
            profile.photo = form.cleaned_data.get("photo") or ""
            profile.gender = form.cleaned_data.get("gender") or ""
            profile.save()

            return self.json_success("Pengguna berhasil diperbarui.")
        return self.json_form_error(form)


class AccountDeleteView(BaseAccountView):
    def post(self, request, slug):
        account_or_response = get_object_or_json(Account, slug=slug)
        if isinstance(account_or_response, JsonResponse):
            return account_or_response
        account = account_or_response

        if account == request.user:
            messages.error(request, "Anda tidak dapat menghapus akun sendiri.")
            return redirect("core:account_list")
        if self.is_developer_account(account):
            messages.error(request, "Pengguna Developer tidak dapat dihapus.")
            return redirect("core:account_list")
        account.delete()
        messages.success(request, "Pengguna berhasil dihapus.")
        return redirect("core:account_list")
