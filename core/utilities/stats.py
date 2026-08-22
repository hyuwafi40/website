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
from core.utilities.constants import JOB_ADMINISTRATOR, JOB_DEVELOPER


def get_dashboard_stats(user):
    user_identifier = user.get_full_name() or user.username
    identifiers = [user_identifier]
    if user.username != user_identifier:
        identifiers.append(user.username)

    personal_stats = [
        {
            "label": "Artikel Saya",
            "icon": "fa-solid fa-newspaper",
            "value": Article.objects.filter(created_by__in=identifiers).count(),
        },
        {
            "label": "Album Saya",
            "icon": "fa-solid fa-folder-open",
            "value": Album.objects.filter(created_by__in=identifiers).count(),
        },
        {
            "label": "Foto Saya",
            "icon": "fa-solid fa-image",
            "value": Photos.objects.filter(created_by__in=identifiers).count(),
        },
    ]

    global_stats = None
    if getattr(user, "job", None) in [JOB_DEVELOPER, JOB_ADMINISTRATOR]:
        global_stats = [
            {
                "label": "Total Artikel",
                "icon": "fa-solid fa-newspaper",
                "value": Article.objects.count(),
            },
            {
                "label": "Total Album",
                "icon": "fa-solid fa-folder-open",
                "value": Album.objects.count(),
            },
            {
                "label": "Total Foto",
                "icon": "fa-solid fa-image",
                "value": Photos.objects.count(),
            },
            {
                "label": "Total Komentar",
                "icon": "fa-solid fa-comments",
                "value": Comment.objects.count(),
            },
            {
                "label": "Kategori",
                "icon": "fa-solid fa-tags",
                "value": Category.objects.count(),
            },
            {
                "label": "Tag",
                "icon": "fa-solid fa-tag",
                "value": Tag.objects.count(),
            },
            {
                "label": "Halaman",
                "icon": "fa-solid fa-file-lines",
                "value": Page.objects.count(),
            },
        ]
        if getattr(user, "job", None) == JOB_DEVELOPER:
            global_stats.extend(
                [
                    {
                        "label": "Hero",
                        "icon": "fa-solid fa-images",
                        "value": Hero.objects.count(),
                    },
                    {
                        "label": "Iklan",
                        "icon": "fa-solid fa-rectangle-ad",
                        "value": Advertisement.objects.count(),
                    },
                ]
            )
    return personal_stats, global_stats
