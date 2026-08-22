from solo.admin import SingletonModelAdmin


class BaseSingletonAdmin(SingletonModelAdmin):
    readonly_fields = ("slug",)
