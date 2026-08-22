from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import redirect, render

from blog.models import Comment
from core.forms.comment import CommentStatusForm
from core.utilities.pagination import paginate
from core.utilities.responses import get_object_or_json
from core.views.base import BaseCommentView


class CommentListView(BaseCommentView):
    template_name = "core/comment.html"
    paginate_by = 10

    def get(self, request):
        queryset = Comment.objects.select_related("article").order_by("-created_at")
        page_obj, page_range = paginate(request, queryset, self.paginate_by)
        form = CommentStatusForm()
        context = {
            "comments": page_obj.object_list,
            "page_obj": page_obj,
            "page_range": page_range,
            "form": form,
        }
        return render(request, self.template_name, context)


class CommentUpdateStatusView(BaseCommentView):
    def post(self, request, pk):
        comment_or_response = get_object_or_json(Comment, pk=pk)
        if isinstance(comment_or_response, JsonResponse):
            return comment_or_response
        comment = comment_or_response

        form = CommentStatusForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return self.json_success("Status komentar berhasil diubah.")
        return self.json_form_error(form)


class CommentDeleteView(BaseCommentView):
    def post(self, request, pk):
        comment_or_response = get_object_or_json(Comment, pk=pk)
        if isinstance(comment_or_response, JsonResponse):
            return comment_or_response
        comment = comment_or_response
        comment.delete()
        messages.success(request, "Komentar berhasil dihapus.")
        return redirect("core:comment_list")
