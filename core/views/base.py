from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic import TemplateView

from core.models.user import Profile
from core.utilities.constants import (
    JOB_ADMINISTRATOR,
    JOB_DEVELOPER,
    JOB_REGULER,
)
from core.utilities.stats import get_dashboard_stats
from core.views.access import (
    AccountAccessMixin,
    AdvertisementAccessMixin,
    AlbumAccessMixin,
    ArticleAccessMixin,
    BrandAccessMixin,
    CategoryAccessMixin,
    CommentAccessMixin,
    HeroAccessMixin,
    PageAccessMixin,
    ResourcesAccessMixin,
    ResourcesResetAccessMixin,
    SchoolAccessMixin,
    TagAccessMixin,
)
from core.views.mixins import JsonFormMixin


class RoleDashboardMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        context["is_developer"] = getattr(user, "job", None) == JOB_DEVELOPER
        context["is_administrator"] = getattr(user, "job", None) == JOB_ADMINISTRATOR
        context["is_reguler"] = getattr(user, "job", None) == JOB_REGULER
        context["role"] = getattr(user, "job", None)
        context["personal_stats"], context["global_stats"] = get_dashboard_stats(user)

        return context


class BaseDashboardView(LoginRequiredMixin, RoleDashboardMixin, TemplateView):
    pass


class BaseProfileView(LoginRequiredMixin, TemplateView):
    def get_profile(self):
        return Profile.objects.get_or_create(account=self.request.user)[0]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile"] = self.get_profile()
        context["account"] = self.request.user
        return context


class BaseArticleView(LoginRequiredMixin, ArticleAccessMixin, View):
    pass


class BaseAlbumView(LoginRequiredMixin, AlbumAccessMixin, View):
    pass


class BaseCategoryView(LoginRequiredMixin, CategoryAccessMixin, JsonFormMixin, View):
    pass


class BaseTagView(LoginRequiredMixin, TagAccessMixin, JsonFormMixin, View):
    pass


class BasePageView(LoginRequiredMixin, PageAccessMixin, View):
    pass


class BaseCommentView(LoginRequiredMixin, CommentAccessMixin, JsonFormMixin, View):
    pass


class BaseBrandView(LoginRequiredMixin, BrandAccessMixin, View):
    pass


class BaseSchoolView(LoginRequiredMixin, SchoolAccessMixin, View):
    pass


class BaseHeroView(LoginRequiredMixin, HeroAccessMixin, JsonFormMixin, View):
    pass


class BaseAdvertisementView(
    LoginRequiredMixin, AdvertisementAccessMixin, JsonFormMixin, View
):
    pass


class BaseAccountView(LoginRequiredMixin, AccountAccessMixin, JsonFormMixin, View):
    def is_developer_account(self, account):
        return account.job == JOB_DEVELOPER


class BaseResourcesView(LoginRequiredMixin, ResourcesAccessMixin, View):
    pass


class ResourcesResetView(LoginRequiredMixin, ResourcesResetAccessMixin, View):
    pass
