from django import forms

from blog.models import Hero
from core.forms.base import FormControlMixin
from core.utilities.helpers import set_placeholders


class HeroForm(FormControlMixin, forms.ModelForm):
    class Meta:
        model = Hero
        fields = ["name", "photo"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        set_placeholders(
            self,
            {
                "name": "Nama hero",
                "photo": "https://example.com/photo.jpg",
            },
        )
