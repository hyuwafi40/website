from django import forms

from blog.models import Comment
from core.forms.base import FormControlMixin


class CommentStatusForm(FormControlMixin, forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["status"]
        widgets = {
            "status": forms.Select(),
        }
