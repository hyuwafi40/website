from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from core.models.user import Account, Profile


@admin.register(Account)
class AccountAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (("Job", {"fields": ("job", "slug")}),)
    add_fieldsets = UserAdmin.add_fieldsets + (("Job", {"fields": ("job",)}),)
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "job",
        "is_active",
        "is_staff",
        "is_superuser",
    )
    list_filter = ("job", "is_staff", "is_superuser", "is_active")
    search_fields = ("username", "first_name", "last_name", "email")
    readonly_fields = ("slug", "created_at", "updated_at")


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "account",
        "city",
        "province",
        "country",
        "created_at",
        "updated_at",
    )
    search_fields = ("account__username", "account__email", "city", "province")
    readonly_fields = ("slug", "created_at", "updated_at")
    fieldsets = (
        (None, {"fields": ("account", "photo", "slug")}),
        ("Kontak", {"fields": ("phone", "mobile", "website")}),
        (
            "Alamat",
            {"fields": ("address", "city", "province", "country", "postal_code")},
        ),
        ("Data Pribadi", {"fields": ("birth_date", "gender", "bio")}),
        (
            "Pekerjaan",
            {
                "fields": (
                    "occupation",
                    "company",
                    "department",
                    "employee_id",
                    "joined_at",
                )
            },
        ),
        ("Media Sosial", {"fields": ("linkedin", "github", "twitter", "instagram")}),
    )
