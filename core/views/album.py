from django.contrib import messages
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render

from blog.models import Album, Photos
from core.forms.album import AlbumForm, PhotoForm
from core.utilities.pagination import paginate
from core.views.base import BaseAlbumView


class AlbumListView(BaseAlbumView):
    template_name = "core/album.html"
    paginate_by = 10

    def get(self, request):
        queryset = (
            self.get_album_queryset()
            .annotate(photo_count=Count("photos"))
            .order_by("-created_at")
        )
        page_obj, page_range = paginate(request, queryset, self.paginate_by)
        for album in page_obj.object_list:
            album.can_manage = self.can_manage_album(album)

        context = {
            "page_obj": page_obj,
            "albums": page_obj.object_list,
            "page_range": page_range,
        }
        return render(request, self.template_name, context)


class AlbumCreateView(BaseAlbumView):
    template_name = "core/album/form_album.html"

    def get(self, request):
        form = AlbumForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = AlbumForm(request.POST)
        if form.is_valid():
            album = form.save(commit=False)
            album.created_by = self.get_user_identifier()
            album.save()
            messages.success(request, "Album berhasil dibuat.")
            return redirect("core:album_list")
        return render(request, self.template_name, {"form": form})


class AlbumUpdateView(BaseAlbumView):
    template_name = "core/album/form_album.html"

    def get_album(self, slug):
        return get_object_or_404(Album, slug=slug)

    def get(self, request, slug):
        album = self.get_album(slug)
        if not self.can_manage_album(album):
            messages.error(
                request, "Anda tidak memiliki akses untuk mengubah album ini."
            )
            return redirect("core:album_list")
        form = AlbumForm(instance=album)
        return render(request, self.template_name, {"form": form})

    def post(self, request, slug):
        album = self.get_album(slug)
        if not self.can_manage_album(album):
            messages.error(
                request, "Anda tidak memiliki akses untuk mengubah album ini."
            )
            return redirect("core:album_list")
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            messages.success(request, "Album berhasil diperbarui.")
            return redirect("core:album_list")
        return render(request, self.template_name, {"form": form})


class AlbumDeleteView(BaseAlbumView):
    def post(self, request, slug):
        album = get_object_or_404(Album, slug=slug)
        if not self.can_manage_album(album):
            messages.error(
                request, "Anda tidak memiliki akses untuk menghapus album ini."
            )
            return redirect("core:album_list")
        album.delete()
        messages.success(request, "Album berhasil dihapus.")
        return redirect("core:album_list")


class AlbumToggleStatusView(BaseAlbumView):
    def post(self, request, slug):
        album = get_object_or_404(Album, slug=slug)
        if not self.can_manage_album(album):
            messages.error(
                request, "Anda tidak memiliki akses untuk mengubah status album ini."
            )
            return redirect("core:album_list")
        album.status = "published" if album.status == "draft" else "draft"
        album.save()
        messages.success(request, "Status album berhasil diubah.")
        return redirect("core:album_list")


class AlbumDetailView(BaseAlbumView):
    template_name = "core/album/detail.html"
    paginate_by = 24

    def get(self, request, slug):
        album = get_object_or_404(Album, slug=slug)
        if not self.can_manage_album(album):
            messages.error(request, "Anda tidak memiliki akses untuk album ini.")
            return redirect("core:album_list")

        photos = album.photos.order_by("-created_at")
        page_obj, page_range = paginate(request, photos, self.paginate_by)
        form = PhotoForm()

        context = {
            "album": album,
            "photos": page_obj.object_list,
            "page_obj": page_obj,
            "page_range": page_range,
            "form": form,
        }
        return render(request, self.template_name, context)


class PhotoListView(BaseAlbumView):
    template_name = "core/album/gallery.html"
    paginate_by = 24

    def get(self, request):
        album_queryset = self.get_album_queryset()
        photos = (
            Photos.objects.select_related("album")
            .filter(album__in=album_queryset)
            .order_by("-created_at")
        )
        page_obj, page_range = paginate(request, photos, self.paginate_by)

        context = {
            "photos": page_obj.object_list,
            "page_obj": page_obj,
            "page_range": page_range,
        }
        return render(request, self.template_name, context)


class PhotoCreateView(BaseAlbumView):
    def post(self, request, slug):
        album = get_object_or_404(Album, slug=slug)
        if not self.can_manage_album(album):
            messages.error(request, "Anda tidak memiliki akses untuk album ini.")
            return redirect("core:album_list")
        form = PhotoForm(request.POST)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.album = album
            photo.created_by = self.get_user_identifier()
            photo.save()
            messages.success(request, "Foto berhasil diunggah.")
            return redirect("core:album_gallery", slug=album.slug)
        messages.error(request, "Gagal mengunggah foto. Periksa kembali isian Anda.")
        return redirect("core:album_gallery", slug=album.slug)


class PhotoDeleteView(BaseAlbumView):
    def post(self, request, slug):
        photo = get_object_or_404(Photos, slug=slug)
        if not self.can_manage_album(photo.album):
            messages.error(
                request, "Anda tidak memiliki akses untuk menghapus foto ini."
            )
            return redirect("core:photo_list")
        album_slug = photo.album.slug
        photo.delete()
        messages.success(request, "Foto berhasil dihapus.")
        return redirect("core:album_gallery", slug=album_slug)
