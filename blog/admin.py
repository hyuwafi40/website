from django.contrib import admin
from blog.models import (
    Advertisement,
    Album,
    Article,
    Category,
    Comment,
    Hero,
    Page,
    Photos,
    Tag,
)


class CreatedByAdminMixin:
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            user = request.user
            full_name = user.get_full_name() or user.username
            obj.created_by = full_name
        super().save_model(request, obj, form, change)


@admin.register(Category)
class CategoryAdmin(CreatedByAdminMixin, admin.ModelAdmin):
    list_display = ("name", "slug", "created_by", "created_at", "updated_at")
    search_fields = ("name",)
    readonly_fields = ("slug", "created_by", "created_at", "updated_at")


@admin.register(Tag)
class TagAdmin(CreatedByAdminMixin, admin.ModelAdmin):
    list_display = ("name", "slug", "created_by", "created_at", "updated_at")
    search_fields = ("name",)
    readonly_fields = ("slug", "created_by", "created_at", "updated_at")


@admin.register(Article)
class ArticleAdmin(CreatedByAdminMixin, admin.ModelAdmin):
    list_display = ("title", "category", "created_by", "created_at", "updated_at")
    list_filter = ("category", "tags")
    search_fields = ("title", "content")
    readonly_fields = ("slug", "created_by", "created_at", "updated_at")
    filter_horizontal = ("tags",)


@admin.register(Album)
class AlbumAdmin(CreatedByAdminMixin, admin.ModelAdmin):
    list_display = ("title", "status", "created_by", "created_at", "updated_at")
    list_filter = ("status",)
    search_fields = ("title", "description")
    readonly_fields = ("slug", "created_by", "created_at", "updated_at")


@admin.register(Photos)
class PhotosAdmin(CreatedByAdminMixin, admin.ModelAdmin):
    list_display = ("title", "album", "created_by", "created_at", "updated_at")
    list_filter = ("album",)
    search_fields = ("title", "caption")
    readonly_fields = ("slug", "created_by", "created_at", "updated_at")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("name", "article", "status", "created_at")
    list_filter = ("status",)
    search_fields = ("name", "email", "content")
    readonly_fields = ("created_at",)


@admin.register(Page)
class PageAdmin(CreatedByAdminMixin, admin.ModelAdmin):
    list_display = ("title", "category", "created_by", "created_at", "updated_at")
    list_filter = ("category", "tags")
    search_fields = ("title", "content")
    readonly_fields = ("slug", "created_by", "created_at", "updated_at")
    filter_horizontal = ("tags",)


@admin.register(Hero)
class HeroAdmin(CreatedByAdminMixin, admin.ModelAdmin):
    list_display = ("name", "created_by", "created_at", "updated_at")
    search_fields = ("name",)
    readonly_fields = ("slug", "created_by", "created_at", "updated_at")


@admin.register(Advertisement)
class AdvertisementAdmin(CreatedByAdminMixin, admin.ModelAdmin):
    list_display = (
        "type",
        "status",
        "enddate",
        "created_by",
        "created_at",
        "updated_at",
    )
    list_filter = ("status", "type")
    search_fields = ("type", "link")
    readonly_fields = ("slug", "created_by", "created_at", "updated_at")
