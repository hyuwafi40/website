from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import redirect, render

from blog.models import Hero
from core.forms.hero import HeroForm
from core.utilities.pagination import paginate
from core.utilities.responses import get_object_or_json
from core.views.base import BaseHeroView


class HeroListView(BaseHeroView):
    template_name = "core/hero.html"
    paginate_by = 10

    def get(self, request):
        queryset = Hero.objects.order_by("-created_at")
        page_obj, page_range = paginate(request, queryset, self.paginate_by)
        form = HeroForm()
        context = {
            "heroes": page_obj.object_list,
            "page_obj": page_obj,
            "page_range": page_range,
            "form": form,
        }
        return render(request, self.template_name, context)


class HeroCreateView(BaseHeroView):
    def post(self, request):
        form = HeroForm(request.POST)
        if form.is_valid():
            hero = form.save(commit=False)
            hero.created_by = self.get_user_identifier()
            hero.save()
            return self.json_success("Hero berhasil dibuat.")
        return self.json_form_error(form)


class HeroUpdateView(BaseHeroView):
    def post(self, request, slug):
        hero_or_response = get_object_or_json(Hero, slug=slug)
        if isinstance(hero_or_response, JsonResponse):
            return hero_or_response
        hero = hero_or_response

        form = HeroForm(request.POST, instance=hero)
        if form.is_valid():
            form.save()
            return self.json_success("Hero berhasil diperbarui.")
        return self.json_form_error(form)


class HeroDeleteView(BaseHeroView):
    def post(self, request, slug):
        hero_or_response = get_object_or_json(Hero, slug=slug)
        if isinstance(hero_or_response, JsonResponse):
            return hero_or_response
        hero = hero_or_response
        hero.delete()
        messages.success(request, "Hero berhasil dihapus.")
        return redirect("core:hero_list")
