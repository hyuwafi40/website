from django.db.models import Count
from django.shortcuts import render
from django.utils.html import strip_tags
from django.views import View

from blog.forms import CommentForm
from blog.models import Advertisement, Article, Category
from core.models.brand import Brand, School


class PublicContextMixin:
    def get_base_context(self, request):
        return {
            "brand": Brand.get_solo(),
            "school": School.get_solo(),
        }

    def render_page(self, request, full_template, partial_template, context):
        if request.htmx:
            return render(request, partial_template, context)
        return render(request, full_template, context)


class BasePublicView(PublicContextMixin, View):
    pass


class ArticleDetailContextMixin(PublicContextMixin):
    def get_article_detail_context(self, request, article, form=None):
        comments = list(article.comments.filter(status="published"))
        published_comment_count = len(comments)
        categories = Category.objects.annotate(article_count=Count("articles"))[:6]
        recent_articles = (
            Article.published.exclude(pk=article.pk)
            .select_related("category")
            .order_by("-created_at")[:5]
        )
        rectangle_ad = Advertisement.active.filter(
            type__in=["large_rectangle", "half_page"]
        ).first()

        description = strip_tags(article.content)[:150]
        if not description:
            description = article.title

        context = self.get_base_context(request)
        context.update(
            {
                "article": article,
                "comments": comments,
                "published_comment_count": published_comment_count,
                "categories": categories,
                "recent_articles": recent_articles,
                "rectangle_ad": rectangle_ad,
                "page_title": article.title,
                "meta_description": description,
                "share_url": request.build_absolute_uri(request.path),
                "form": form if form is not None else CommentForm(),
            }
        )
        return context
