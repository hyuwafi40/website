import os
from datetime import datetime

from django.conf import settings
from django.core.management import call_command

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
from core.models.brand import Brand, School

MODEL_LABELS = [
    "blog.Category",
    "blog.Tag",
    "blog.Album",
    "blog.Article",
    "blog.Page",
    "blog.Photos",
    "blog.Comment",
    "blog.Hero",
    "blog.Advertisement",
    "core.Brand",
    "core.School",
]

RESET_MODEL_LABELS = [
    "blog.Comment",
    "blog.Photos",
    "blog.Article",
    "blog.Page",
    "blog.Album",
    "blog.Hero",
    "blog.Advertisement",
    "blog.Category",
    "blog.Tag",
    "core.Brand",
    "core.School",
]

MODEL_CLASSES = {
    "blog.Category": Category,
    "blog.Tag": Tag,
    "blog.Album": Album,
    "blog.Article": Article,
    "blog.Page": Page,
    "blog.Photos": Photos,
    "blog.Comment": Comment,
    "blog.Hero": Hero,
    "blog.Advertisement": Advertisement,
    "core.Brand": Brand,
    "core.School": School,
}

MODEL_DISPLAY_NAMES = {
    "blog.Category": "Kategori",
    "blog.Tag": "Tag",
    "blog.Album": "Album",
    "blog.Article": "Artikel",
    "blog.Page": "Halaman",
    "blog.Photos": "Foto",
    "blog.Comment": "Komentar",
    "blog.Hero": "Hero",
    "blog.Advertisement": "Iklan",
    "core.Brand": "Brand",
    "core.School": "Sekolah",
}

BACKUP_DIR = settings.BASE_DIR / "backup"


def ensure_backup_dir():
    os.makedirs(BACKUP_DIR, exist_ok=True)


def get_timestamp():
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def validate_model_label(model_label):
    if model_label and model_label not in MODEL_CLASSES:
        raise ValueError("Model tidak dikenal.")


def create_backup(model_label=None):
    validate_model_label(model_label)
    ensure_backup_dir()
    if model_label:
        filename = f"{model_label.replace('.', '_')}_{get_timestamp()}.json"
        file_path = BACKUP_DIR / filename
        call_command("dumpdata", model_label, output=str(file_path))
    else:
        filename = f"all_{get_timestamp()}.json"
        file_path = BACKUP_DIR / filename
        call_command("dumpdata", *MODEL_LABELS, output=str(file_path))
    return file_path


def restore_backup(model_label, file_path):
    validate_model_label(model_label)
    if model_label:
        model_class = MODEL_CLASSES.get(model_label)
        model_class.objects.all().delete()
        call_command("loaddata", str(file_path))
    else:
        reset_data()
        call_command("loaddata", str(file_path))


def reset_data():
    for label in RESET_MODEL_LABELS:
        MODEL_CLASSES[label].objects.all().delete()


def get_model_counts():
    return [
        {
            "name": MODEL_DISPLAY_NAMES.get(label, label),
            "count": MODEL_CLASSES[label].objects.count(),
        }
        for label in MODEL_LABELS
    ]
