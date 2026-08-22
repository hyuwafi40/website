from functools import lru_cache

from django.db.models import Count

from blog.models import Advertisement, Album, Article, Category, Comment, Page, Photos


@lru_cache(maxsize=1)
def get_public_categories():
    return list(Category.objects.annotate(article_count=Count("articles")))


@lru_cache(maxsize=1)
def get_public_pages():
    return list(Page.objects.all())


@lru_cache(maxsize=1)
def get_index_stats():
    return {
        "articles": Article.published.count(),
        "albums": Album.published.count(),
        "photos": Photos.objects.filter(album__status="published").count(),
        "categories": Category.objects.count(),
        "comments": Comment.objects.filter(status="published").count(),
    }


@lru_cache(maxsize=1)
def get_horizontal_ad():
    return Advertisement.active.filter(type__in=["leaderboard", "billboard"]).first()
