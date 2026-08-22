from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

from blog.constants import (
    ADVERTISEMENT_STATUS_CHOICES,
    ADVERTISEMENT_TYPE_CHOICES,
    COMMENT_STATUS_CHOICES,
    DEFAULT_CREATED_BY,
    STATUS_CHOICES,
)
from blog.managers import ActiveAdvertisementManager, PublishedManager
from blog.utils import generate_unique_slug
from blog.validators import validate_http_url, validate_image_url


class CreatedAtModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        abstract = True


class TimeStampedModel(CreatedAtModel):
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True


class SlugMixin(TimeStampedModel):
    slug = models.SlugField(max_length=150, unique=True, blank=True, editable=False)
    created_by = models.CharField(
        max_length=150,
        blank=True,
        default=DEFAULT_CREATED_BY,
        editable=False,
    )

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.slug:
            source_value = getattr(self, self.slug_source_field, None)
            self.slug = generate_unique_slug(self, "slug", source_value)
        super().save(*args, **kwargs)


class Category(SlugMixin):
    name = models.CharField(max_length=100, unique=True)
    slug_source_field = "name"

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ["-created_at"]

    def __str__(self):
        return self.name


class Tag(SlugMixin):
    name = models.CharField(max_length=100, unique=True)
    slug_source_field = "name"

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"
        ordering = ["-created_at"]

    def __str__(self):
        return self.name


class Article(SlugMixin):
    title = models.CharField(max_length=200, unique=True)
    thumbnail = models.URLField(max_length=255, validators=[validate_image_url])
    content = CKEditor5Field()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="draft")
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="articles",
    )
    tags = models.ManyToManyField(Tag, blank=True, related_name="articles")
    slug_source_field = "title"

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class Album(SlugMixin):
    title = models.CharField(max_length=200, unique=True)
    thumbnail = models.URLField(max_length=255, validators=[validate_image_url])
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="draft")
    slug_source_field = "title"

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        verbose_name = "Album"
        verbose_name_plural = "Albums"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class Photos(SlugMixin):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="photos")
    title = models.CharField(max_length=200, unique=True)
    photo = models.URLField(max_length=255, validators=[validate_image_url])
    caption = models.TextField()
    slug_source_field = "title"

    class Meta:
        verbose_name = "Photo"
        verbose_name_plural = "Photos"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class Comment(CreatedAtModel):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    name = models.CharField(max_length=100)
    email = models.EmailField()
    content = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=COMMENT_STATUS_CHOICES,
        default="pending",
    )

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        ordering = ["-created_at"]

    def __str__(self):
        return f"Komentar oleh {self.name} pada {self.article.title}"


class Page(SlugMixin):
    title = models.CharField(max_length=200, unique=True)
    thumbnail = models.URLField(max_length=255, validators=[validate_image_url])
    content = CKEditor5Field()
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="pages",
    )
    tags = models.ManyToManyField(Tag, blank=True, related_name="pages")
    slug_source_field = "title"

    class Meta:
        verbose_name = "Page"
        verbose_name_plural = "Pages"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class Hero(SlugMixin):
    name = models.CharField(max_length=200, unique=True)
    photo = models.URLField(max_length=255, validators=[validate_image_url])
    slug_source_field = "name"

    class Meta:
        verbose_name = "Hero"
        verbose_name_plural = "Heroes"
        ordering = ["-created_at"]

    def __str__(self):
        return self.name


class Advertisement(SlugMixin):
    type = models.CharField(
        max_length=50,
        choices=ADVERTISEMENT_TYPE_CHOICES,
        default="leaderboard",
    )
    image = models.URLField(
        max_length=255,
        validators=[validate_image_url],
    )
    link = models.URLField(
        max_length=255,
        validators=[validate_http_url],
    )
    enddate = models.DateTimeField()
    status = models.CharField(
        max_length=20,
        choices=ADVERTISEMENT_STATUS_CHOICES,
        default="active",
    )
    slug_source_field = "type"

    objects = models.Manager()
    active = ActiveAdvertisementManager()

    class Meta:
        verbose_name = "Advertisement"
        verbose_name_plural = "Advertisements"
        ordering = ["-created_at"]

    def __str__(self):
        return f"Iklan {self.get_type_display()}"
