from django.db.models.signals import post_save
from django.dispatch import receiver

from core.models.brand import Brand, School
from core.models.user import Account, Profile
from core.utilities.services import get_brand, get_school


@receiver(post_save, sender=Account)
def create_profile(sender, instance, created, **kwargs):
    if kwargs.get("raw"):
        return
    if created:
        Profile.objects.get_or_create(account=instance)


@receiver(post_save, sender=Brand)
def clear_brand_cache(sender, **kwargs):
    get_brand.cache_clear()


@receiver(post_save, sender=School)
def clear_school_cache(sender, **kwargs):
    get_school.cache_clear()
