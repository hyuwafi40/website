from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from blog.models import Page
from core.forms.page import PageForm
from core.utilities.pagination import paginate
from core.views.base import BasePageView


class PageListView(BasePageView):
    template_name = "core/page.html"
    paginate_by = 10

    def get(self, request):
        queryset = (
            Page.objects.select_related("category")
            .prefetch_related("tags")
            .order_by("-created_at")
        )
        page_obj, page_range = paginate(request, queryset, self.paginate_by)

        context = {
            "pages": page_obj.object_list,
            "page_obj": page_obj,
            "page_range": page_range,
        }
        return render(request, self.template_name, context)


class PageCreateView(BasePageView):
    template_name = "core/page/form.html"

    def get(self, request):
        form = PageForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = PageForm(request.POST)
        if form.is_valid():
            page = form.save(commit=False)
            page.created_by = self.get_user_identifier()
            page.save()
            form.save_m2m()
            messages.success(request, "Halaman berhasil dibuat.")
            return redirect("core:page_list")
        return render(request, self.template_name, {"form": form})


class PageUpdateView(BasePageView):
    template_name = "core/page/form.html"

    def get_page(self, slug):
        return get_object_or_404(Page, slug=slug)

    def get(self, request, slug):
        page = self.get_page(slug)
        form = PageForm(instance=page)
        return render(request, self.template_name, {"form": form})

    def post(self, request, slug):
        page = self.get_page(slug)
        form = PageForm(request.POST, instance=page)
        if form.is_valid():
            form.save()
            messages.success(request, "Halaman berhasil diperbarui.")
            return redirect("core:page_list")
        return render(request, self.template_name, {"form": form})


class PageDeleteView(BasePageView):
    def post(self, request, slug):
        page = get_object_or_404(Page, slug=slug)
        page.delete()
        messages.success(request, "Halaman berhasil dihapus.")
        return redirect("core:page_list")
