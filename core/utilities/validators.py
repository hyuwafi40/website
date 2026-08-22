from django.core.exceptions import ValidationError
from django.core.validators import validate_email as django_validate_email


def validate_username(value):
    if not value:
        raise ValidationError("Username tidak boleh kosong.")
    if " " in value:
        raise ValidationError("Username tidak boleh mengandung spasi.")


def validate_email(value):
    django_validate_email(value)


def validate_photo_url(value):
    if value and not value.startswith(("http://", "https://")):
        raise ValidationError("URL foto harus menggunakan skema http atau https.")


def validate_phone(value):
    if value and not value.isdigit():
        raise ValidationError("Nomor telepon hanya boleh berisi angka.")
