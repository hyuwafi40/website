from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import redirect

from core.forms.profile import AccountForm, ProfileForm
from core.views.base import BaseProfileView


class ProfileDetailView(BaseProfileView):
    template_name = "core/profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_edit"] = False
        return context


class ProfileUpdateView(BaseProfileView):
    template_name = "core/profile.html"

    def get_form_sections(self, account_form, profile_form):
        return [
            {
                "title": "Akun",
                "icon": "fa-solid fa-user",
                "desc": "Nama dan email",
                "fields": [account_form[field] for field in account_form.fields],
            },
            {
                "title": "Foto & Kontak",
                "icon": "fa-solid fa-address-card",
                "desc": "Foto profil, telepon, dan website",
                "fields": [
                    profile_form[field]
                    for field in ["photo", "phone", "mobile", "website"]
                ],
            },
            {
                "title": "Alamat",
                "icon": "fa-solid fa-location-dot",
                "desc": "Lokasi tempat tinggal",
                "fields": [
                    profile_form[field]
                    for field in [
                        "address",
                        "city",
                        "province",
                        "country",
                        "postal_code",
                    ]
                ],
            },
            {
                "title": "Data Pribadi",
                "icon": "fa-solid fa-id-card",
                "desc": "Tanggal lahir, gender, bio",
                "fields": [
                    profile_form[field] for field in ["birth_date", "gender", "bio"]
                ],
            },
            {
                "title": "Pekerjaan",
                "icon": "fa-solid fa-briefcase",
                "desc": "Informasi pekerjaan",
                "fields": [
                    profile_form[field]
                    for field in [
                        "occupation",
                        "company",
                        "department",
                        "employee_id",
                        "joined_at",
                    ]
                ],
            },
            {
                "title": "Media Sosial",
                "icon": "fa-solid fa-share-nodes",
                "desc": "Akun media sosial",
                "fields": [
                    profile_form[field]
                    for field in ["linkedin", "github", "twitter", "instagram"]
                ],
            },
        ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        account_form = AccountForm(instance=self.request.user)
        profile_form = ProfileForm(instance=context["profile"])
        context["is_edit"] = True
        context["account_form"] = account_form
        context["profile_form"] = profile_form
        context["form_sections"] = self.get_form_sections(account_form, profile_form)
        return context

    def post(self, request, *args, **kwargs):
        user = request.user
        profile = self.get_profile()
        account_form = AccountForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, instance=profile)

        if account_form.is_valid() and profile_form.is_valid():
            account = account_form.save(commit=False)
            password = account_form.cleaned_data.get("password")
            if password:
                account.set_password(password)
            account.save()
            profile_form.save()
            if password:
                update_session_auth_hash(request, account)
            messages.success(request, "Profil berhasil diperbarui.")
            return redirect("core:profile")

        context = self.get_context_data(**kwargs)
        context["account_form"] = account_form
        context["profile_form"] = profile_form
        context["form_sections"] = self.get_form_sections(account_form, profile_form)
        return self.render_to_response(context)
