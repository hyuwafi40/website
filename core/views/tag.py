from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import redirect, render

from blog.models import Tag
from core.forms.tag import TagForm
from core.utilities.pagination import paginate
from core.utilities.responses import get_object_or_json
from core.views.base import BaseTagView


class TagListView(BaseTagView):
    template_name = "core/tag.html"
    paginate_by = 10

    def get(self, request):
        queryset = Tag.objects.order_by("-created_at")
        page_obj, page_range = paginate(request, queryset, self.paginate_by)
        form = TagForm()
        context = {
            "tags": page_obj.object_list,
            "page_obj": page_obj,
            "page_range": page_range,
            "form": form,
        }
        return render(request, self.template_name, context)


class TagCreateView(BaseTagView):
    def post(self, request):
        form = TagForm(request.POST)
        if form.is_valid():
            tag = form.save(commit=False)
            tag.created_by = self.get_user_identifier()
            tag.save()
            return self.json_success("Tag berhasil dibuat.")
        return self.json_form_error(form)


class TagUpdateView(BaseTagView):
    def post(self, request, slug):
        tag_or_response = get_object_or_json(Tag, slug=slug)
        if isinstance(tag_or_response, JsonResponse):
            return tag_or_response
        tag = tag_or_response

        form = TagForm(request.POST, instance=tag)
        if form.is_valid():
            form.save()
            return self.json_success("Tag berhasil diperbarui.")
        return self.json_form_error(form)


class TagDeleteView(BaseTagView):
    def post(self, request, slug):
        tag_or_response = get_object_or_json(Tag, slug=slug)
        if isinstance(tag_or_response, JsonResponse):
            return tag_or_response
        tag = tag_or_response
        tag.delete()
        messages.success(request, "Tag berhasil dihapus.")
        return redirect("core:tag_list")
