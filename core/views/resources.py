import tempfile

from django.contrib import messages
from django.http import FileResponse, JsonResponse
from django.shortcuts import render

from core.utilities.resources import (
    create_backup,
    get_model_counts,
    reset_data,
    restore_backup,
)
from core.views.base import BaseResourcesView, ResourcesResetView


class ResourcesView(BaseResourcesView):
    template_name = "core/resources.html"

    def get(self, request):
        context = {"model_counts": get_model_counts()}
        return render(request, self.template_name, context)


class BackupView(BaseResourcesView):
    def post(self, request):
        model_label = request.POST.get("model_label", "").strip() or None
        try:
            file_path = create_backup(model_label)
            messages.success(request, f"Backup berhasil dibuat: {file_path.name}")
            return FileResponse(
                file_path.open("rb"),
                as_attachment=True,
                filename=file_path.name,
            )
        except Exception as e:
            return JsonResponse({"success": False, "message": str(e)}, status=500)


class RestoreView(BaseResourcesView):
    def post(self, request):
        model_label = request.POST.get("model_label", "").strip() or None
        uploaded_file = request.FILES.get("file")

        if not uploaded_file:
            return JsonResponse(
                {"success": False, "message": "File backup wajib diunggah."},
                status=400,
            )

        if not uploaded_file.name.endswith(".json"):
            return JsonResponse(
                {"success": False, "message": "Format file harus JSON."},
                status=400,
            )

        try:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".json") as tmp:
                for chunk in uploaded_file.chunks():
                    tmp.write(chunk)
                tmp_path = tmp.name

            restore_backup(model_label, tmp_path)
            messages.success(request, "Restore berhasil.")
            return JsonResponse({"success": True})
        except Exception as e:
            return JsonResponse({"success": False, "message": str(e)}, status=500)


class ResetView(ResourcesResetView):
    def post(self, request):
        try:
            reset_data()
            messages.success(request, "Reset data berhasil.")
            return JsonResponse({"success": True})
        except Exception as e:
            return JsonResponse({"success": False, "message": str(e)}, status=500)
