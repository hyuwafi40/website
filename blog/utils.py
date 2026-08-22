import uuid

from django.utils.text import slugify


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
