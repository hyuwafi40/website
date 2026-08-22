from core.utilities.constants import JOB_ADMINISTRATOR, JOB_DEVELOPER, JOB_REGULER

MENUS = [
    {
        "label": "Home",
        "items": [
            {
                "label": "Dashboard",
                "url": "#",
                "url_name": "core:index",
                "icon": "fa-solid fa-computer",
                "roles": [JOB_DEVELOPER],
            },
            {
                "label": "Dashboard",
                "url": "#",
                "url_name": "core:index",
                "icon": "fa-solid fa-computer",
                "roles": [JOB_ADMINISTRATOR],
            },
            {
                "label": "Dashboard",
                "url": "#",
                "url_name": "core:index",
                "icon": "fa-solid fa-computer",
                "roles": [JOB_REGULER],
            },
            {
                "label": "Profile",
                "url": "#",
                "url_name": "core:profile",
                "icon": "fa-solid fa-id-card",
                "roles": [JOB_DEVELOPER, JOB_ADMINISTRATOR, JOB_REGULER],
            },
            {
                "label": "Lihat Website",
                "url": "#",
                "url_name": "blog:index",
                "icon": "fa-solid fa-globe",
                "roles": [JOB_DEVELOPER, JOB_ADMINISTRATOR, JOB_REGULER],
            },
        ],
    },
    {
        "label": "Article",
        "items": [
            {
                "label": "Buat Artikel",
                "url": "#",
                "url_name": "core:article_create",
                "icon": "fa-solid fa-pen-to-square",
                "roles": [JOB_DEVELOPER, JOB_ADMINISTRATOR, JOB_REGULER],
            },
            {
                "label": "Daftar Artikel",
                "url": "#",
                "url_name": "core:article_list",
                "icon": "fa-solid fa-list",
                "roles": [JOB_DEVELOPER, JOB_ADMINISTRATOR, JOB_REGULER],
            },
        ],
    },
    {
        "label": "Album",
        "items": [
            {
                "label": "Buat Album",
                "url": "#",
                "url_name": "core:album_create",
                "icon": "fa-solid fa-folder-plus",
                "roles": [JOB_DEVELOPER, JOB_ADMINISTRATOR, JOB_REGULER],
            },
            {
                "label": "Daftar Album",
                "url": "#",
                "url_name": "core:album_list",
                "icon": "fa-solid fa-folder-open",
                "roles": [JOB_DEVELOPER, JOB_ADMINISTRATOR, JOB_REGULER],
            },
            {
                "label": "Semua Foto",
                "url": "#",
                "url_name": "core:photo_list",
                "icon": "fa-solid fa-image",
                "roles": [JOB_DEVELOPER, JOB_ADMINISTRATOR, JOB_REGULER],
            },
        ],
    },
    {
        "label": "Management",
        "items": [
            {
                "label": "Atur Kategori",
                "url": "#",
                "url_name": "core:category_list",
                "icon": "fa-solid fa-tags",
                "roles": [JOB_DEVELOPER, JOB_ADMINISTRATOR],
            },
            {
                "label": "Atur Tag",
                "url": "#",
                "url_name": "core:tag_list",
                "icon": "fa-solid fa-tag",
                "roles": [JOB_DEVELOPER, JOB_ADMINISTRATOR],
            },
            {
                "label": "Atur Halaman",
                "url": "#",
                "url_name": "core:page_list",
                "icon": "fa-solid fa-file-lines",
                "roles": [JOB_DEVELOPER, JOB_ADMINISTRATOR],
            },
            {
                "label": "Kelola Komentar",
                "url": "#",
                "url_name": "core:comment_list",
                "icon": "fa-solid fa-comments",
                "roles": [JOB_DEVELOPER, JOB_ADMINISTRATOR],
            },
        ],
    },
    {
        "label": "Configuration",
        "items": [
            {
                "label": "Brand",
                "url": "#",
                "url_name": "core:brand",
                "icon": "fa-solid fa-copyright",
                "roles": [JOB_DEVELOPER],
            },
            {
                "label": "School",
                "url": "#",
                "url_name": "core:school",
                "icon": "fa-solid fa-school",
                "roles": [JOB_DEVELOPER, JOB_ADMINISTRATOR],
            },
            {
                "label": "Hero",
                "url": "#",
                "url_name": "core:hero_list",
                "icon": "fa-solid fa-images",
                "roles": [JOB_DEVELOPER],
            },
            {
                "label": "Advertisement",
                "url": "#",
                "url_name": "core:advertisement_list",
                "icon": "fa-solid fa-rectangle-ad",
                "roles": [JOB_DEVELOPER],
            },
            {
                "label": "Pengguna",
                "url": "#",
                "url_name": "core:account_list",
                "icon": "fa-solid fa-users",
                "roles": [JOB_DEVELOPER, JOB_ADMINISTRATOR],
            },
            {
                "label": "Backup & Restore",
                "url": "#",
                "url_name": "core:resources",
                "icon": "fa-solid fa-database",
                "roles": [JOB_DEVELOPER, JOB_ADMINISTRATOR],
            },
        ],
    },
]
