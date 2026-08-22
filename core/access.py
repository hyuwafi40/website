from core.utilities.constants import JOB_ADMINISTRATOR, JOB_DEVELOPER, JOB_REGULER


def is_developer(user):
    return user.is_authenticated and getattr(user, "job", None) == JOB_DEVELOPER


def is_administrator(user):
    return user.is_authenticated and getattr(user, "job", None) == JOB_ADMINISTRATOR


def is_reguler(user):
    return user.is_authenticated and getattr(user, "job", None) == JOB_REGULER


def has_role(user, roles):
    if not user.is_authenticated:
        return False
    return getattr(user, "job", None) in roles


def filter_menu_items(menus, user):
    if not user.is_authenticated:
        return []
    filtered = []
    for group in menus:
        items = [item for item in group["items"] if has_role(user, item["roles"])]
        if items:
            filtered.append({"label": group["label"], "items": items})
    return filtered
