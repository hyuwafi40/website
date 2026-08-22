from django.forms import CheckboxInput, CheckboxSelectMultiple, RadioSelect


class FormControlMixin:
    form_control_excluded_fields = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name in self.form_control_excluded_fields:
                continue
            if isinstance(
                field.widget,
                (CheckboxInput, CheckboxSelectMultiple, RadioSelect),
            ):
                continue
            current_class = field.widget.attrs.get("class", "")
            field.widget.attrs["class"] = f"{current_class} form-control".strip()
