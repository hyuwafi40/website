from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from core.models.base import TimeStampedModel
from core.utilities.constants import GENDER_CHOICES, JOB_CHOICES, JOB_ROLE_FLAGS
from core.utilities.managers import AccountManager
from core.utilities.services import generate_unique_slug


class Account(AbstractUser, TimeStampedModel):
    job = models.CharField(max_length=50, choices=JOB_CHOICES, default="reguler")
    slug = models.SlugField(max_length=150, unique=True, blank=True, editable=False)

    objects = AccountManager()

    class Meta:
        verbose_name = "Account"
        verbose_name_plural = "Accounts"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_slug(self, "slug", self.username)
        if self.pk:
            old = Account.objects.filter(pk=self.pk).only("job").first()
            if old and old.job != self.job:
                flags = JOB_ROLE_FLAGS.get(self.job, {})
                for field, value in flags.items():
                    setattr(self, field, value)
        else:
            flags = JOB_ROLE_FLAGS.get(self.job, {})
            for field, value in flags.items():
                setattr(self, field, value)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.get_full_name() or self.username


class Profile(TimeStampedModel):
    account = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile",
    )
    photo = models.URLField(max_length=255, blank=True, null=True)
    slug = models.SlugField(max_length=150, unique=True, blank=True, editable=False)

    phone = models.CharField(max_length=30, blank=True, null=True)
    mobile = models.CharField(max_length=30, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    province = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    gender = models.CharField(
        max_length=20, choices=GENDER_CHOICES, blank=True, null=True
    )
    bio = models.TextField(blank=True, null=True)
    website = models.URLField(max_length=255, blank=True, null=True)
    linkedin = models.URLField(max_length=255, blank=True, null=True)
    github = models.URLField(max_length=255, blank=True, null=True)
    twitter = models.URLField(max_length=255, blank=True, null=True)
    instagram = models.URLField(max_length=255, blank=True, null=True)
    occupation = models.CharField(max_length=150, blank=True, null=True)
    company = models.CharField(max_length=150, blank=True, null=True)
    department = models.CharField(max_length=150, blank=True, null=True)
    employee_id = models.CharField(max_length=50, blank=True, null=True)
    joined_at = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_slug(self, "slug", self.account.username)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Profil {self.account.username}"
