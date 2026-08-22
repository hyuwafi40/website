import uuid
from functools import lru_cache

from django.utils.text import slugify

from core.models.brand import Brand, School


def generate_unique_slug(instance, slug_field, source_value, max_length=150):
    if not source_value:
        source_value = str(uuid.uuid4())[:8]
    slug = slugify(source_value)[:max_length]
    if not slug:
        slug = str(uuid.uuid4())[:8]
    unique_slug = slug
    counter = 1
    model_class = instance.__class__
    queryset = model_class.objects.filter(**{slug_field: unique_slug})
    if instance.pk:
        queryset = queryset.exclude(pk=instance.pk)
    while queryset.exists():
        suffix = f"-{counter}"
        unique_slug = f"{slug[:max_length - len(suffix)]}{suffix}"
        counter += 1
        queryset = model_class.objects.filter(**{slug_field: unique_slug})
        if instance.pk:
            queryset = queryset.exclude(pk=instance.pk)
    return unique_slug


def generate_username(first_name, last_name, email):
    base = first_name.lower().strip() or "user"
    if last_name:
        base += last_name.lower().strip()
    username = slugify(base)
    if not username:
        username = email.split("@")[0] if email else str(uuid.uuid4())[:8]
    return username[:150]


@lru_cache(maxsize=1)
def get_brand():
    return Brand.get_solo()


@lru_cache(maxsize=1)
def get_school():
    return School.get_solo()
