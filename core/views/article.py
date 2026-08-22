from django.contrib import messages
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render

from blog.models import Article
from core.forms.article import ArticleForm
from core.utilities.pagination import paginate
from core.views.base import BaseArticleView


class ArticleListView(BaseArticleView):
    template_name = "core/article.html"
    paginate_by = 10

    def get(self, request):
        queryset = (
            self.get_article_queryset()
            .annotate(comment_count=Count("comments"))
            .order_by("-created_at")
        )
        page_obj, page_range = paginate(request, queryset, self.paginate_by)
        for article in page_obj.object_list:
            article.can_manage = self.can_manage_article(article)

        context = {
            "page_obj": page_obj,
            "articles": page_obj.object_list,
            "page_range": page_range,
        }
        return render(request, self.template_name, context)


class ArticleCreateView(BaseArticleView):
    template_name = "core/article/form.html"

    def get(self, request):
        form = ArticleForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.created_by = self.get_user_identifier()
            article.save()
            form.save_m2m()
            messages.success(request, "Artikel berhasil dibuat.")
            return redirect("core:article_list")
        return render(request, self.template_name, {"form": form})


class ArticleUpdateView(BaseArticleView):
    template_name = "core/article/form.html"

    def get_article(self, slug):
        return get_object_or_404(Article, slug=slug)

    def get(self, request, slug):
        article = self.get_article(slug)
        if not self.can_manage_article(article):
            messages.error(
                request, "Anda tidak memiliki akses untuk mengubah artikel ini."
            )
            return redirect("core:article_list")
        form = ArticleForm(instance=article)
        return render(request, self.template_name, {"form": form})

    def post(self, request, slug):
        article = self.get_article(slug)
        if not self.can_manage_article(article):
            messages.error(
                request, "Anda tidak memiliki akses untuk mengubah artikel ini."
            )
            return redirect("core:article_list")
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, "Artikel berhasil diperbarui.")
            return redirect("core:article_list")
        return render(request, self.template_name, {"form": form})


class ArticleDeleteView(BaseArticleView):
    def post(self, request, slug):
        article = get_object_or_404(Article, slug=slug)
        if not self.can_manage_article(article):
            messages.error(
                request, "Anda tidak memiliki akses untuk menghapus artikel ini."
            )
            return redirect("core:article_list")
        article.delete()
        messages.success(request, "Artikel berhasil dihapus.")
        return redirect("core:article_list")


class ArticleToggleStatusView(BaseArticleView):
    def post(self, request, slug):
        article = get_object_or_404(Article, slug=slug)
        if not self.can_manage_article(article):
            messages.error(
                request, "Anda tidak memiliki akses untuk mengubah status artikel ini."
            )
            return redirect("core:article_list")
        article.status = "published" if article.status == "draft" else "draft"
        article.save()
        messages.success(request, "Status artikel berhasil diubah.")
        return redirect("core:article_list")
