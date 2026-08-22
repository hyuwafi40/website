from django import forms
from django.contrib.auth import get_user_model

from core.forms.base import FormControlMixin
from core.utilities.constants import GENDER_CHOICES, JOB_DEVELOPER
from core.utilities.helpers import set_empty_label, set_placeholders


class AccountAdminForm(FormControlMixin, forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(),
        required=False,
        label="Password",
        help_text="Kosongkan jika tidak ingin mengubah password.",
    )
    photo = forms.URLField(
        required=False,
        label="Foto Profil",
    )
    gender = forms.ChoiceField(
        required=False,
        choices=GENDER_CHOICES,
        label="Jenis Kelamin",
    )

    class Meta:
        model = get_user_model()
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "job",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if "job" in self.fields:
            self.fields["job"].choices = [
                choice
                for choice in self.fields["job"].choices
                if choice[0] != JOB_DEVELOPER
            ]
        set_empty_label(self, "gender", "Pilih jenis kelamin")
        set_placeholders(
            self,
            {
                "username": "Username",
                "first_name": "Nama depan",
                "last_name": "Nama belakang",
                "email": "email@domain.com",
                "photo": "https://example.com/photo.jpg",
                "password": "Password",
            },
        )
