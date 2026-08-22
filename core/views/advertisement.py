from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import redirect, render

from blog.models import Advertisement
from core.forms.advertisement import AdvertisementForm
from core.utilities.pagination import paginate
from core.utilities.responses import get_object_or_json
from core.views.base import BaseAdvertisementView


class AdvertisementListView(BaseAdvertisementView):
    template_name = "core/advertisement.html"
    paginate_by = 10

    def get(self, request):
        queryset = Advertisement.objects.order_by("-created_at")
        page_obj, page_range = paginate(request, queryset, self.paginate_by)
        form = AdvertisementForm()
        context = {
            "advertisements": page_obj.object_list,
            "page_obj": page_obj,
            "page_range": page_range,
            "form": form,
        }
        return render(request, self.template_name, context)


class AdvertisementCreateView(BaseAdvertisementView):
    def post(self, request):
        form = AdvertisementForm(request.POST)
        if form.is_valid():
            advertisement = form.save(commit=False)
            advertisement.created_by = self.get_user_identifier()
            advertisement.save()
            return self.json_success("Iklan berhasil dibuat.")
        return self.json_form_error(form)


class AdvertisementUpdateView(BaseAdvertisementView):
    def post(self, request, slug):
        advertisement_or_response = get_object_or_json(Advertisement, slug=slug)
        if isinstance(advertisement_or_response, JsonResponse):
            return advertisement_or_response
        advertisement = advertisement_or_response

        form = AdvertisementForm(request.POST, instance=advertisement)
        if form.is_valid():
            form.save()
            return self.json_success("Iklan berhasil diperbarui.")
        return self.json_form_error(form)


class AdvertisementDeleteView(BaseAdvertisementView):
    def post(self, request, slug):
        advertisement_or_response = get_object_or_json(Advertisement, slug=slug)
        if isinstance(advertisement_or_response, JsonResponse):
            return advertisement_or_response
        advertisement = advertisement_or_response
        advertisement.delete()
        messages.success(request, "Iklan berhasil dihapus.")
        return redirect("core:advertisement_list")
