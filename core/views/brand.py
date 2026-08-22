from django.contrib import messages
from django.shortcuts import redirect, render

from core.forms.brand import BrandForm
from core.utilities.services import get_brand
from core.views.base import BaseBrandView


class BrandDetailView(BaseBrandView):
    template_name = "core/brand.html"

    def get(self, request):
        brand = get_brand()
        context = {
            "brand": brand,
            "is_edit": False,
        }
        return render(request, self.template_name, context)


class BrandUpdateView(BaseBrandView):
    template_name = "core/brand.html"

    def get(self, request):
        brand = get_brand()
        form = BrandForm(instance=brand)
        context = {
            "brand": brand,
            "form": form,
            "is_edit": True,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        brand = get_brand()
        form = BrandForm(request.POST, instance=brand)
        if form.is_valid():
            form.save()
            messages.success(request, "Brand berhasil diperbarui.")
            return redirect("core:brand")
        context = {
            "brand": brand,
            "form": form,
            "is_edit": True,
        }
        return render(request, self.template_name, context)
