from core.access import filter_menu_items
from core.menu import MENUS
from core.utilities.services import get_brand, get_school


def core_context(request):
    menus = []
    page_heading = "Dashboard"

    if request.user.is_authenticated:
        menus = filter_menu_items(MENUS, request.user)
        current_view = request.resolver_match.view_name

        heading_map = {
            "core:index": "Dashboard",
            "core:profile": "Profile",
            "core:profile_edit": "Profile Edit",
            "core:article_edit": "Edit Artikel",
            "core:album_edit": "Edit Album",
            "core:album_gallery": "Detail Album",
            "core:photo_list": "Semua Foto",
            "core:category_list": "Kategori",
            "core:tag_list": "Tag",
            "core:tag_edit": "Edit Tag",
            "core:page_list": "Halaman",
            "core:page_edit": "Edit Halaman",
            "core:comment_list": "Komentar",
            "core:brand": "Brand",
            "core:brand_update": "Edit Brand",
            "core:school": "School",
            "core:school_update": "Edit School",
            "core:hero_list": "Hero",
            "core:hero_edit": "Edit Hero",
            "core:advertisement_list": "Iklan",
            "core:advertisement_edit": "Edit Iklan",
            "core:account_list": "Pengguna",
            "core:account_edit": "Edit Pengguna",
            "core:resources": "Backup & Restore",
        }

        page_heading = heading_map.get(current_view, "Dashboard")

        if page_heading == "Dashboard" and current_view != "core:index":
            for group in MENUS:
                for item in group["items"]:
                    if item.get("url_name") == current_view:
                        page_heading = item["label"]
                        break
                else:
                    continue
                break

    brand = get_brand()
    school = get_school()

    return {
        "menus": menus,
        "brand": brand,
        "school": school,
        "page_heading": page_heading,
    }
