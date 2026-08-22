from django import forms
from django.contrib.auth import get_user_model

from core.forms.base import FormControlMixin
from core.models.user import Profile
from core.utilities.helpers import set_empty_label, set_placeholders


class AccountForm(FormControlMixin, forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(),
        required=False,
        label="Password Baru",
        help_text="Kosongkan jika tidak ingin mengubah password.",
    )

    class Meta:
        model = get_user_model()
        fields = ["first_name", "last_name", "email"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        set_placeholders(
            self,
            {
                "first_name": "Nama depan",
                "last_name": "Nama belakang",
                "email": "nama@domain.com",
                "password": "Kata sandi baru",
            },
        )


class ProfileForm(FormControlMixin, forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            "photo",
            "phone",
            "mobile",
            "address",
            "city",
            "province",
            "country",
            "postal_code",
            "birth_date",
            "gender",
            "bio",
            "website",
            "linkedin",
            "github",
            "twitter",
            "instagram",
            "occupation",
            "company",
            "department",
            "employee_id",
            "joined_at",
        ]
        widgets = {
            "birth_date": forms.DateInput(attrs={"type": "date"}),
            "joined_at": forms.DateInput(attrs={"type": "date"}),
            "bio": forms.Textarea(attrs={"rows": 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        set_empty_label(self, "gender", "Pilih jenis kelamin")
        set_placeholders(
            self,
            {
                "photo": "https://example.com/photo.jpg",
                "phone": "08xxxxxxxxxx",
                "mobile": "08xxxxxxxxxx",
                "address": "Jl. Contoh No. 1",
                "city": "Kota",
                "province": "Provinsi",
                "country": "Negara",
                "postal_code": "12345",
                "bio": "Ceritakan tentang Anda",
                "website": "https://example.com",
                "linkedin": "https://linkedin.com/in/username",
                "github": "https://github.com/username",
                "twitter": "https://twitter.com/username",
                "instagram": "https://instagram.com/username",
                "occupation": "Pekerjaan",
                "company": "Perusahaan",
                "department": "Departemen",
                "employee_id": "ID Karyawan",
            },
        )
