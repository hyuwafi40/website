from django import forms

from blog.models import Album, Photos
from core.forms.base import FormControlMixin
from core.utilities.helpers import set_placeholders


class AlbumForm(FormControlMixin, forms.ModelForm):
    class Meta:
        model = Album
        fields = ["title", "thumbnail", "description", "status"]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        set_placeholders(
            self,
            {
                "title": "Judul album",
                "thumbnail": "https://example.com/thumb.jpg",
                "description": "Deskripsi album",
            },
        )


class PhotoForm(FormControlMixin, forms.ModelForm):
    class Meta:
        model = Photos
        fields = ["title", "photo", "caption"]
        widgets = {
            "caption": forms.Textarea(attrs={"rows": 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        set_placeholders(
            self,
            {
                "title": "Judul foto",
                "photo": "https://example.com/photo.jpg",
                "caption": "Caption foto",
            },
        )
