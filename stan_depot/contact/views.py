from django.conf import settings
from django.core.mail import EmailMessage

from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from .forms import ContactForm
from .models import Place


class ContactPageView(FormView):
    template_name = "contact/home.html"
    form_class = ContactForm
    success_url = "thanks/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["places"] = Place.objects.all()
        return context

    def form_valid(self, form):
        subject = form.cleaned_data["email"] + " " + form.cleaned_data["subject"]
        email = form.cleaned_data["email"]
        message = form.cleaned_data["message"]
        mail = EmailMessage(subject, message, email, [settings.EMAIL_HOST_USER])
        mail.send()
        return super().form_valid(form)


class ThankYouPageView(TemplateView):
    template_name = "contact/thanks.html"
