from django.contrib import admin
from core.admin.base import BaseSingletonAdmin
from core.models.brand import Brand, School


@admin.register(Brand)
class BrandAdmin(BaseSingletonAdmin):
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "name",
                    "description",
                    "version",
                    "tahun",
                    "logo",
                    "developer",
                    "slug",
                )
            },
        ),
        (
            "Social Media",
            {
                "fields": (
                    "instagram",
                    "youtube",
                    "tiktok",
                    "facebook",
                )
            },
        ),
    )


@admin.register(School)
class SchoolAdmin(BaseSingletonAdmin):
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "name",
                    "logo",
                    "slug",
                )
            },
        ),
        (
            "Kontak",
            {
                "fields": (
                    "address",
                    "phone",
                    "email",
                    "website",
                )
            },
        ),
        (
            "Data Sekolah",
            {
                "fields": (
                    "npsn",
                    "nss",
                    "school_type",
                    "school_status",
                    "accreditation",
                    "curriculum",
                    "established_year",
                )
            },
        ),
        (
            "Kepala Sekolah",
            {
                "fields": (
                    "headmaster_name",
                    "headmaster_nip",
                )
            },
        ),
        (
            "Alamat",
            {
                "fields": (
                    "village",
                    "district",
                    "city",
                    "province",
                    "postal_code",
                )
            },
        ),
        (
            "Visi Misi",
            {
                "fields": (
                    "motto",
                    "vision",
                    "mission",
                    "goals",
                )
            },
        ),
    )
