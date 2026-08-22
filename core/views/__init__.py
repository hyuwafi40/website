from core.views.account import (
    AccountCreateView,
    AccountDeleteView,
    AccountListView,
    AccountUpdateView,
)
from core.views.advertisement import (
    AdvertisementCreateView,
    AdvertisementDeleteView,
    AdvertisementListView,
    AdvertisementUpdateView,
)
from core.views.album import (
    AlbumCreateView,
    AlbumDeleteView,
    AlbumDetailView,
    AlbumListView,
    AlbumToggleStatusView,
    AlbumUpdateView,
    PhotoCreateView,
    PhotoDeleteView,
    PhotoListView,
)
from core.views.article import (
    ArticleCreateView,
    ArticleDeleteView,
    ArticleListView,
    ArticleToggleStatusView,
    ArticleUpdateView,
)
from core.views.brand import BrandDetailView, BrandUpdateView
from core.views.category import (
    CategoryCreateView,
    CategoryDeleteView,
    CategoryListView,
    CategoryUpdateView,
)
from core.views.comment import (
    CommentDeleteView,
    CommentListView,
    CommentUpdateStatusView,
)
from core.views.hero import (
    HeroCreateView,
    HeroDeleteView,
    HeroListView,
    HeroUpdateView,
)
from core.views.index import IndexView
from core.views.page import (
    PageCreateView,
    PageDeleteView,
    PageListView,
    PageUpdateView,
)
from core.views.profile import ProfileDetailView, ProfileUpdateView
from core.views.resources import BackupView, ResetView, ResourcesView, RestoreView
from core.views.school import SchoolDetailView, SchoolUpdateView
from core.views.tag import (
    TagCreateView,
    TagDeleteView,
    TagListView,
    TagUpdateView,
)

__all__ = [
    "IndexView",
    "ProfileDetailView",
    "ProfileUpdateView",
    "ArticleListView",
    "ArticleCreateView",
    "ArticleUpdateView",
    "ArticleDeleteView",
    "ArticleToggleStatusView",
    "AlbumListView",
    "AlbumCreateView",
    "AlbumUpdateView",
    "AlbumDeleteView",
    "AlbumToggleStatusView",
    "AlbumDetailView",
    "PhotoListView",
    "PhotoCreateView",
    "PhotoDeleteView",
    "CategoryListView",
    "CategoryCreateView",
    "CategoryUpdateView",
    "CategoryDeleteView",
    "TagListView",
    "TagCreateView",
    "TagUpdateView",
    "TagDeleteView",
    "PageListView",
    "PageCreateView",
    "PageUpdateView",
    "PageDeleteView",
    "CommentListView",
    "CommentUpdateStatusView",
    "CommentDeleteView",
    "BrandDetailView",
    "BrandUpdateView",
    "SchoolDetailView",
    "SchoolUpdateView",
    "HeroListView",
    "HeroCreateView",
    "HeroUpdateView",
    "HeroDeleteView",
    "AdvertisementListView",
    "AdvertisementCreateView",
    "AdvertisementUpdateView",
    "AdvertisementDeleteView",
    "AccountListView",
    "AccountCreateView",
    "AccountUpdateView",
    "AccountDeleteView",
    "ResourcesView",
    "BackupView",
    "RestoreView",
    "ResetView",
]
