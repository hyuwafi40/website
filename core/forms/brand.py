from django import forms

from core.forms.base import FormControlMixin
from core.models.brand import Brand
from core.utilities.helpers import set_placeholders


class BrandForm(FormControlMixin, forms.ModelForm):
    class Meta:
        model = Brand
        fields = [
            "name",
            "description",
            "version",
            "tahun",
            "logo",
            "instagram",
            "youtube",
            "tiktok",
            "facebook",
            "developer",
        ]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        set_placeholders(
            self,
            {
                "name": "Nama brand",
                "description": "Deskripsi brand",
                "version": "Versi",
                "tahun": "Tahun",
                "logo": "https://example.com/logo.png",
                "instagram": "https://instagram.com/username",
                "youtube": "https://youtube.com/@channel",
                "tiktok": "https://tiktok.com/@username",
                "facebook": "https://facebook.com/username",
                "developer": "Nama developer",
            },
        )
