from django.contrib import admin

from .forms import PlaceCreateForm, PlaceUpdateForm
from stan_depot.careers.models import Place


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    form = PlaceCreateForm
    list_display = ("name", "address")
    list_display_links = ("name",)
    list_filter = ("country", "city")
    ordering = ["address"]
    search_fields = ["name", "address", "street"]

    def get_form(self, request, obj=None, change=False, **kwargs):
        if obj:
            kwargs["form"] = PlaceUpdateForm
        return super().get_form(request, obj, change, **kwargs)
