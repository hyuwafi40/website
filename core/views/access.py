from django.contrib import messages
from django.shortcuts import redirect

from blog.models import Album, Article
from core.utilities.constants import JOB_ADMINISTRATOR, JOB_DEVELOPER


class UserIdentifierMixin:
    def get_user_identifier(self):
        user = self.request.user
        return user.get_full_name() or user.username


class StaffOnlyAccessMixin(UserIdentifierMixin):
    access_denied_message = "Anda tidak memiliki akses."
    allowed_jobs = [JOB_DEVELOPER, JOB_ADMINISTRATOR]

    def has_access(self):
        return getattr(self.request.user, "job", None) in self.allowed_jobs

    def dispatch(self, request, *args, **kwargs):
        if not self.has_access():
            messages.error(request, self.access_denied_message)
            return redirect("core:index")
        return super().dispatch(request, *args, **kwargs)


class ArticleAccessMixin(UserIdentifierMixin):
    def get_article_queryset(self):
        user = self.request.user
        identifiers = [self.get_user_identifier()]
        if user.username != identifiers[0]:
            identifiers.append(user.username)
        if user.job in [JOB_DEVELOPER, JOB_ADMINISTRATOR]:
            return Article.objects.all()
        return Article.objects.filter(created_by__in=identifiers)

    def can_manage_article(self, article):
        user = self.request.user
        if user.job in [JOB_DEVELOPER, JOB_ADMINISTRATOR]:
            return True
        identifier = self.get_user_identifier()
        return article.created_by == identifier or article.created_by == user.username


class AlbumAccessMixin(UserIdentifierMixin):
    def get_album_queryset(self):
        user = self.request.user
        identifiers = [self.get_user_identifier()]
        if user.username != identifiers[0]:
            identifiers.append(user.username)
        if user.job in [JOB_DEVELOPER, JOB_ADMINISTRATOR]:
            return Album.objects.all()
        return Album.objects.filter(created_by__in=identifiers)

    def can_manage_album(self, album):
        user = self.request.user
        if user.job in [JOB_DEVELOPER, JOB_ADMINISTRATOR]:
            return True
        identifier = self.get_user_identifier()
        return album.created_by == identifier or album.created_by == user.username


class CategoryAccessMixin(StaffOnlyAccessMixin):
    access_denied_message = "Anda tidak memiliki akses ke manajemen kategori."


class TagAccessMixin(StaffOnlyAccessMixin):
    access_denied_message = "Anda tidak memiliki akses ke manajemen tag."


class PageAccessMixin(StaffOnlyAccessMixin):
    access_denied_message = "Anda tidak memiliki akses ke manajemen halaman."


class CommentAccessMixin(StaffOnlyAccessMixin):
    access_denied_message = "Anda tidak memiliki akses ke manajemen komentar."


class BrandAccessMixin(StaffOnlyAccessMixin):
    access_denied_message = "Anda tidak memiliki akses ke manajemen brand."
    allowed_jobs = [JOB_DEVELOPER]


class SchoolAccessMixin(StaffOnlyAccessMixin):
    access_denied_message = "Anda tidak memiliki akses ke manajemen sekolah."
    allowed_jobs = [JOB_DEVELOPER, JOB_ADMINISTRATOR]


class HeroAccessMixin(StaffOnlyAccessMixin):
    access_denied_message = "Anda tidak memiliki akses ke manajemen hero."
    allowed_jobs = [JOB_DEVELOPER]


class AdvertisementAccessMixin(StaffOnlyAccessMixin):
    access_denied_message = "Anda tidak memiliki akses ke manajemen iklan."
    allowed_jobs = [JOB_DEVELOPER]


class AccountAccessMixin(StaffOnlyAccessMixin):
    access_denied_message = "Anda tidak memiliki akses ke manajemen pengguna."
    allowed_jobs = [JOB_DEVELOPER, JOB_ADMINISTRATOR]


class ResourcesAccessMixin(StaffOnlyAccessMixin):
    access_denied_message = "Anda tidak memiliki akses ke Backup & Restore."
    allowed_jobs = [JOB_DEVELOPER, JOB_ADMINISTRATOR]


class ResourcesResetAccessMixin(StaffOnlyAccessMixin):
    access_denied_message = "Hanya Developer yang dapat melakukan reset."
    allowed_jobs = [JOB_DEVELOPER]
