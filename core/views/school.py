from django.contrib import messages
from django.shortcuts import redirect, render

from core.forms.school import SchoolForm
from core.utilities.services import get_school
from core.views.base import BaseSchoolView


class SchoolDetailView(BaseSchoolView):
    template_name = "core/school.html"

    def get(self, request):
        school = get_school()
        context = {
            "school": school,
            "is_edit": False,
        }
        return render(request, self.template_name, context)


class SchoolUpdateView(BaseSchoolView):
    template_name = "core/school.html"

    def get(self, request):
        school = get_school()
        form = SchoolForm(instance=school)
        context = {
            "school": school,
            "form": form,
            "is_edit": True,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        school = get_school()
        form = SchoolForm(request.POST, instance=school)
        if form.is_valid():
            form.save()
            messages.success(request, "School berhasil diperbarui.")
            return redirect("core:school")
        context = {
            "school": school,
            "form": form,
            "is_edit": True,
        }
        return render(request, self.template_name, context)
