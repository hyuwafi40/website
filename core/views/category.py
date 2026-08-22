from django.contrib import messages
from django.db.models import ProtectedError
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from blog.models import Category
from core.forms.category import CategoryForm
from core.utilities.pagination import paginate
from core.utilities.responses import get_object_or_json
from core.views.base import BaseCategoryView


class CategoryListView(BaseCategoryView):
    template_name = "core/category.html"
    paginate_by = 10

    def get(self, request):
        queryset = Category.objects.order_by("-created_at")
        page_obj, page_range = paginate(request, queryset, self.paginate_by)
        form = CategoryForm()
        context = {
            "categories": page_obj.object_list,
            "page_obj": page_obj,
            "page_range": page_range,
            "form": form,
        }
        return render(request, self.template_name, context)


class CategoryCreateView(BaseCategoryView):
    def post(self, request):
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.created_by = self.get_user_identifier()
            category.save()
            return self.json_success("Kategori berhasil dibuat.")
        return self.json_form_error(form)


class CategoryUpdateView(BaseCategoryView):
    def post(self, request, slug):
        category_or_response = get_object_or_json(Category, slug=slug)
        if isinstance(category_or_response, JsonResponse):
            return category_or_response
        category = category_or_response

        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return self.json_success("Kategori berhasil diperbarui.")
        return self.json_form_error(form)


class CategoryDeleteView(BaseCategoryView):
    def post(self, request, slug):
        category = get_object_or_404(Category, slug=slug)
        try:
            category.delete()
        except ProtectedError:
            messages.error(
                request, "Kategori masih digunakan oleh artikel atau halaman."
            )
            return redirect("core:category_list")
        messages.success(request, "Kategori berhasil dihapus.")
        return redirect("core:category_list")
