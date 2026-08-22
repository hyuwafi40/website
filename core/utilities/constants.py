JOB_DEVELOPER = "developer"
JOB_ADMINISTRATOR = "administrator"
JOB_REGULER = "reguler"

JOB_CHOICES = [
    (JOB_DEVELOPER, "Developer"),
    (JOB_ADMINISTRATOR, "Administrator"),
    (JOB_REGULER, "Reguler"),
]

JOB_ROLE_FLAGS = {
    JOB_DEVELOPER: {"is_active": True, "is_staff": True, "is_superuser": True},
    JOB_ADMINISTRATOR: {"is_active": True, "is_staff": True, "is_superuser": False},
    JOB_REGULER: {"is_active": True, "is_staff": False, "is_superuser": False},
}

GENDER_CHOICES = [
    ("male", "Laki-laki"),
    ("female", "Perempuan"),
    ("other", "Lainnya"),
]
