from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import ListView
from django.views import defaults as default_views

from stan_depot.blog.models import Post

urlpatterns = [
    path("", ListView.as_view(template_name="pages/home.html", queryset=Post.published.all()[:3]), name="home"),
    path("contact/", include("stan_depot.contact.urls"), name="contact"),
    path("markdownx/", include("markdownx.urls")),
    path("careers/", include("stan_depot.careers.urls"), name="careers"),
    path("blog/", include("stan_depot.blog.urls"), name="blog"),
    path(settings.ADMIN_URL, admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += [
        path("api-auth/", include("rest_framework.urls")),
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
