from django.conf import settings


def settings_context(_request):
    return {"GOOGLE_API_KEY": settings.GOOGLE_API_KEY}
