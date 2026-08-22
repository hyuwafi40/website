from django.http import JsonResponse


def get_object_or_json(model, **kwargs):
    try:
        return model.objects.get(**kwargs)
    except model.DoesNotExist:
        return JsonResponse(
            {"success": False, "message": "Data tidak ditemukan."},
            status=404,
        )
