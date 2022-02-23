from django.contrib import admin

from stan_depot.careers.models import JobOffer


@admin.register(JobOffer)
class JobOfferAdmin(admin.ModelAdmin):
    list_display = ("title", "location", "compensation_min", "compensation_max", "status")
    list_display_links = ("title",)
    search_fields = ("title", "created", "modified", "location__name",)
    list_filter = ("status", "location__street")
