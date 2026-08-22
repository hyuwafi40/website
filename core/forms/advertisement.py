from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone

from blog.models import Advertisement
from core.forms.base import FormControlMixin
from core.utilities.helpers import set_placeholders


class AdvertisementForm(FormControlMixin, forms.ModelForm):
    enddate = forms.DateTimeField(
        label="Tanggal Akhir",
        widget=forms.DateTimeInput(
            attrs={"type": "datetime-local"},
            format="%Y-%m-%dT%H:%M",
        ),
        input_formats=["%Y-%m-%dT%H:%M", "%Y-%m-%dT%H:%M:%S"],
    )

    class Meta:
        model = Advertisement
        fields = ["type", "image", "link", "enddate", "status"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        set_placeholders(
            self,
            {
                "image": "https://example.com/iklan.jpg",
                "link": "https://example.com",
            },
        )

    def clean_enddate(self):
        enddate = self.cleaned_data.get("enddate")
        status = self.cleaned_data.get("status")
        if status == "active" and enddate and enddate <= timezone.now():
            raise ValidationError(
                "Tanggal akhir iklan harus di masa depan jika status aktif."
            )
        return enddate
