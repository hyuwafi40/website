from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget

from blog.models import Page
from core.forms.base import FormControlMixin
from core.utilities.helpers import set_placeholders


class PageForm(FormControlMixin, forms.ModelForm):
    class Meta:
        model = Page
        fields = ["title", "thumbnail", "category", "tags", "content"]
        widgets = {
            "content": CKEditor5Widget(),
            "tags": forms.CheckboxSelectMultiple(attrs={"class": "tag-checkbox-list"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        set_placeholders(
            self,
            {
                "title": "Judul halaman",
                "thumbnail": "https://example.com/image.jpg",
            },
        )
