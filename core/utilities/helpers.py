def set_placeholders(form, mapping):
    for field_name, placeholder in mapping.items():
        if field_name in form.fields:
            form.fields[field_name].widget.attrs["placeholder"] = placeholder


def set_widget_attrs(form, field_name, attrs):
    if field_name in form.fields:
        form.fields[field_name].widget.attrs.update(attrs)


def set_empty_label(form, field_name, label):
    if field_name in form.fields:
        choices = list(form.fields[field_name].choices)
        if not any(value == "" for value, _ in choices):
            choices.insert(0, ("", label))
        form.fields[field_name].choices = choices
