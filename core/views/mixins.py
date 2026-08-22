from django.contrib import messages
from django.http import JsonResponse


class JsonFormMixin:
    def json_success(self, message=None):
        if message:
            messages.success(self.request, message)
        return JsonResponse({"success": True})

    def json_form_error(self, form):
        return JsonResponse(
            {"success": False, "errors": form.errors.get_json_data()},
            status=400,
        )

    def json_error(self, message=None, status=400):
        return JsonResponse(
            {"success": False, "message": message},
            status=status,
        )
