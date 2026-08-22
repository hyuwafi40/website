from django.contrib import messages
from django.db.models import Count, Q
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.html import strip_tags

from blog.forms import CommentForm
from blog.mixins import ArticleDetailContextMixin, BasePublicView
from blog.models import (
    Advertisement,
    Album,
    Article,
    Category,
    Hero,
    Page,
)
from blog.services import get_horizontal_ad, get_index_stats
from core.utilities.pagination import paginate


class IndexView(BasePublicView):
    def get(self, request):
        articles = Article.published.select_related("category").order_by("-created_at")[
            :6
        ]
        albums = Album.published.prefetch_related("photos").order_by("-created_at")[:6]
        categories = Category.objects.annotate(article_count=Count("articles"))[:6]
        heroes = Hero.objects.order_by("-created_at")[:3]
        horizontal_ad = get_horizontal_ad()

        pengumuman = (
            Article.published.filter(category__slug="pengumuman")
            .select_related("category")
            .order_by("-created_at")[:3]
        )

        agenda = (
            Article.published.filter(category__slug="agenda")
            .select_related("category")
            .order_by("-created_at")[:3]
        )

        prestasi = (
            Article.published.filter(category__slug="prestasi")
            .select_related("category")
            .order_by("-created_at")[:3]
        )

        context = self.get_base_context(request)
        context.update(
            {
                "articles": articles,
                "albums": albums,
                "categories": categories,
                "heroes": heroes,
                "horizontal_ad": horizontal_ad,
                "pengumuman": pengumuman,
                "agenda": agenda,
                "prestasi": prestasi,
                "stats": get_index_stats(),
                "page_title": "Beranda",
                "meta_description": (
                    context["school"].motto
                    if context["school"].motto
                    else f"Website resmi {context['school'].name}"
                ),
            }
        )
        return self.render_page(
            request,
            "blog/index.html",
            "blog/partial/index.html",
            context,
        )


class ArticleListView(BasePublicView):
    def get(self, request):
        articles = Article.published.select_related("category").prefetch_related("tags")
        page_obj, page_range = paginate(request, articles, 9)
        context = self.get_base_context(request)
        context.update(
            {
                "articles": page_obj.object_list,
                "page_obj": page_obj,
                "page_range": page_range,
                "page_title": "Artikel",
                "meta_description": "Daftar artikel terbaru",
            }
        )
        return self.render_page(
            request,
            "blog/article.html",
            "blog/partial/article.html",
            context,
        )


class ArticleDetailView(ArticleDetailContextMixin, BasePublicView):
    def get(self, request, slug):
        article = get_object_or_404(
            Article.published.select_related("category").prefetch_related("tags"),
            slug=slug,
        )
        context = self.get_article_detail_context(request, article)
        return self.render_page(
            request,
            "blog/detail/article.html",
            "blog/partial/detail/article.html",
            context,
        )


class CommentCreateView(ArticleDetailContextMixin, BasePublicView):
    def post(self, request, article_slug):
        article = get_object_or_404(Article.published, slug=article_slug)
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.status = "pending"
            comment.save()

            comments = list(article.comments.filter(status="published"))

            if request.htmx:
                context = {
                    "article": article,
                    "comments": comments,
                    "form": CommentForm(),
                    "form_success": True,
                }
                return render(request, "blog/partial/detail/comments.html", context)

            messages.success(
                request, "Komentar berhasil dikirim dan menunggu moderasi."
            )
            return redirect("blog:article_detail", slug=article.slug)

        comments = list(article.comments.filter(status="published"))

        if request.htmx:
            context = {
                "article": article,
                "comments": comments,
                "form": form,
                "form_success": False,
            }
            return render(request, "blog/partial/detail/comments.html", context)

        context = self.get_article_detail_context(request, article, form=form)
        return render(request, "blog/detail/article.html", context)


class PageListView(BasePublicView):
    def get(self, request):
        pages = Page.objects.select_related("category").prefetch_related("tags")
        page_obj, page_range = paginate(request, pages, 9)
        context = self.get_base_context(request)
        context.update(
            {
                "pages": page_obj.object_list,
                "page_obj": page_obj,
                "page_range": page_range,
                "page_title": "Halaman",
                "meta_description": "Daftar halaman resmi sekolah",
            }
        )
        return self.render_page(
            request,
            "blog/page.html",
            "blog/partial/page.html",
            context,
        )


class PageDetailView(BasePublicView):
    def get(self, request, slug):
        page = get_object_or_404(
            Page.objects.select_related("category").prefetch_related("tags"),
            slug=slug,
        )
        context = self.get_base_context(request)
        context.update(
            {
                "page": page,
                "page_title": page.title,
                "meta_description": strip_tags(page.content)[:150],
            }
        )
        return self.render_page(
            request,
            "blog/detail/page.html",
            "blog/partial/detail/page.html",
            context,
        )


class CategoryListView(BasePublicView):
    def get(self, request):
        categories = Category.objects.annotate(article_count=Count("articles"))
        page_obj, page_range = paginate(request, categories, 12)
        context = self.get_base_context(request)
        context.update(
            {
                "categories": page_obj.object_list,
                "page_obj": page_obj,
                "page_range": page_range,
                "page_title": "Kategori",
                "meta_description": "Daftar kategori artikel",
            }
        )
        return self.render_page(
            request,
            "blog/category.html",
            "blog/partial/category.html",
            context,
        )


class CategoryDetailView(BasePublicView):
    def get(self, request, slug):
        category = get_object_or_404(Category, slug=slug)
        articles = Article.published.filter(category=category).select_related(
            "category"
        )
        page_obj, page_range = paginate(request, articles, 9)
        context = self.get_base_context(request)
        context.update(
            {
                "category": category,
                "articles": page_obj.object_list,
                "page_obj": page_obj,
                "page_range": page_range,
                "page_title": f"Kategori {category.name}",
                "meta_description": f"Kategori {category.name} - {page_obj.paginator.count} artikel",
            }
        )
        return self.render_page(
            request,
            "blog/detail/category.html",
            "blog/partial/detail/category.html",
            context,
        )


class SearchView(BasePublicView):
    def get(self, request):
        query = request.GET.get("q", "").strip()[:100]
        results = Article.published.none()
        if query:
            results = Article.published.filter(
                Q(title__icontains=query)
                | Q(content__icontains=query)
                | Q(created_by__icontains=query)
            ).distinct()
        page_obj, page_range = paginate(request, results, 9)
        context = self.get_base_context(request)
        context.update(
            {
                "query": query,
                "results": page_obj.object_list,
                "page_obj": page_obj,
                "page_range": page_range,
                "page_title": "Pencarian",
                "meta_description": (
                    f"Hasil pencarian untuk {query}" if query else "Pencarian konten"
                ),
                "results_count": page_obj.paginator.count,
            }
        )
        return self.render_page(
            request,
            "blog/search.html",
            "blog/partial/search.html",
            context,
        )


class AlbumListView(BasePublicView):
    def get(self, request):
        albums = Album.published.prefetch_related("photos")
        page_obj, page_range = paginate(request, albums, 9)
        context = self.get_base_context(request)
        context.update(
            {
                "albums": page_obj.object_list,
                "page_obj": page_obj,
                "page_range": page_range,
                "page_title": "Album",
                "meta_description": "Galeri album foto sekolah",
            }
        )
        return self.render_page(
            request,
            "blog/album.html",
            "blog/partial/album.html",
            context,
        )


class AlbumDetailView(BasePublicView):
    def get(self, request, slug):
        album = get_object_or_404(
            Album.published.prefetch_related("photos"),
            slug=slug,
        )
        photos = album.photos.all()
        photo_count = photos.count()
        context = self.get_base_context(request)
        context.update(
            {
                "album": album,
                "photos": photos,
                "photo_count": photo_count,
                "page_title": album.title,
                "meta_description": f"{album.title} - {photo_count} foto",
            }
        )
        return self.render_page(
            request,
            "blog/detail/album.html",
            "blog/partial/detail/album.html",
            context,
        )
