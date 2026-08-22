from core.urls.album import urlpatterns as album_urlpatterns
from core.urls.article import urlpatterns as article_urlpatterns
from core.urls.brand import urlpatterns as brand_urlpatterns
from core.urls.category import urlpatterns as category_urlpatterns
from core.urls.comment import urlpatterns as comment_urlpatterns
from core.urls.hero import urlpatterns as hero_urlpatterns
from core.urls.index import app_name, urlpatterns as index_urlpatterns
from core.urls.page import urlpatterns as page_urlpatterns
from core.urls.profile import urlpatterns as profile_urlpatterns
from core.urls.school import urlpatterns as school_urlpatterns
from core.urls.tag import urlpatterns as tag_urlpatterns
from core.urls.advertisement import urlpatterns as advertisement_urlpatterns
from core.urls.account import urlpatterns as account_urlpatterns
from core.urls.resources import urlpatterns as resources_urlpatterns

urlpatterns = (
    index_urlpatterns
    + profile_urlpatterns
    + article_urlpatterns
    + album_urlpatterns
    + category_urlpatterns
    + tag_urlpatterns
    + page_urlpatterns
    + comment_urlpatterns
    + brand_urlpatterns
    + school_urlpatterns
    + hero_urlpatterns
    + advertisement_urlpatterns
    + account_urlpatterns
    + resources_urlpatterns
)
