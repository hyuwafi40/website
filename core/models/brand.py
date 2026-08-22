from django.db import models
from django.utils.text import slugify
from core.models.base import BaseSingletonModel


class Brand(BaseSingletonModel):
    name = models.CharField(max_length=150)
    description = models.TextField()
    version = models.CharField(max_length=50)
    tahun = models.CharField(max_length=4)
    logo = models.URLField(max_length=255)
    instagram = models.URLField(
        max_length=255,
        default="https://www.instagram.com/hamdayuwafii/",
    )
    youtube = models.URLField(
        max_length=255,
        default="https://www.youtube.com/@hamdayuwafii",
    )
    tiktok = models.URLField(
        max_length=255,
        default="https://www.tiktok.com/@hamdayuwafii",
    )
    facebook = models.URLField(
        max_length=255,
        default="https://web.facebook.com/hamdayuwafii/",
    )
    developer = models.CharField(max_length=150, default="Hamdan Yuwafi")
    slug = models.SlugField(unique=True, blank=True, editable=False)

    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brands"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class School(BaseSingletonModel):
    name = models.CharField(max_length=150, unique=True)
    address = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    website = models.URLField(max_length=255, blank=True, null=True)
    logo = models.URLField(max_length=255, blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, editable=False)

    npsn = models.CharField(max_length=20, blank=True, null=True)
    nss = models.CharField(max_length=20, blank=True, null=True)
    school_type = models.CharField(max_length=100, blank=True, null=True)
    school_status = models.CharField(max_length=50, blank=True, null=True)
    accreditation = models.CharField(max_length=10, blank=True, null=True)
    curriculum = models.CharField(max_length=100, blank=True, null=True)
    headmaster_name = models.CharField(max_length=150, blank=True, null=True)
    headmaster_nip = models.CharField(max_length=50, blank=True, null=True)
    established_year = models.CharField(max_length=4, blank=True, null=True)
    district = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    province = models.CharField(max_length=100, blank=True, null=True)
    village = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    motto = models.TextField(blank=True, null=True)
    vision = models.TextField(blank=True, null=True)
    mission = models.TextField(blank=True, null=True)
    goals = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "School"
        verbose_name_plural = "Schools"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
