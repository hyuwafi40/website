from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from blog.models import Advertisement, Album, Article, Category, Comment, Page, Photos
from blog.services import (
    get_horizontal_ad,
    get_index_stats,
    get_public_categories,
    get_public_pages,
)


@receiver([post_save, post_delete], sender=Category)
def clear_category_cache(sender, **kwargs):
    get_public_categories.cache_clear()
    get_index_stats.cache_clear()


@receiver([post_save, post_delete], sender=Page)
def clear_page_cache(sender, **kwargs):
    get_public_pages.cache_clear()
    get_index_stats.cache_clear()


@receiver([post_save, post_delete], sender=Article)
def clear_article_cache(sender, **kwargs):
    get_index_stats.cache_clear()


@receiver([post_save, post_delete], sender=Album)
def clear_album_cache(sender, **kwargs):
    get_index_stats.cache_clear()


@receiver([post_save, post_delete], sender=Photos)
def clear_photos_cache(sender, **kwargs):
    get_index_stats.cache_clear()


@receiver([post_save, post_delete], sender=Comment)
def clear_comment_cache(sender, **kwargs):
    get_index_stats.cache_clear()


@receiver([post_save, post_delete], sender=Advertisement)
def clear_advertisement_cache(sender, **kwargs):
    get_horizontal_ad.cache_clear()
