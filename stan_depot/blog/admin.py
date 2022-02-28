from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = ("title", "hero", "content", "status", "publish")
    list_display = ("title", "status", 'publish')
    list_display_links = ("title",)
    search_fields = ("title", "created", "modified", "content",)
    list_filter = ("status", )
