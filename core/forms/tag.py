from django import forms

from blog.models import Tag
from core.forms.base import FormControlMixin
from core.utilities.helpers import set_placeholders


class TagForm(FormControlMixin, forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        set_placeholders(self, {"name": "Nama tag"})
