from django.core.exceptions import ValidationError


def validate_http_url(value):
    if not value.startswith(("http://", "https://")):
        raise ValidationError("URL harus menggunakan skema http atau https.")


def validate_image_url(value):
    validate_http_url(value)
