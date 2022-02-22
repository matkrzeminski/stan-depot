from django.conf import settings
from django.core.mail import EmailMessage

from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from rest_framework.generics import ListAPIView

from .forms import ContactForm
from .models import Place
from .serializers import PlaceSerializer
from .utils import permissions


class ContactPageView(FormView):
    template_name = "contact/home.html"
    form_class = ContactForm
    success_url = "thanks/"

    def form_valid(self, form):
        subject = form.cleaned_data["email"] + " " + form.cleaned_data["subject"]
        email = form.cleaned_data["email"]
        message = form.cleaned_data["message"]
        mail = EmailMessage(subject, message, email, [settings.EMAIL_HOST_USER])
        mail.send()
        return super().form_valid(form)


class ThankYouPageView(TemplateView):
    template_name = "contact/thanks.html"


class PlaceListAPIView(ListAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    permission_classes = [permissions.ReadOnly]
