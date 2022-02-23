from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.mail import EmailMessage
from django.urls import reverse
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import FormMixin

from .forms import JobOfferEmailForm
from .models import JobOffer


class JobOfferListView(ListView):
    model = JobOffer
    template_name = "careers/list.html"
    context_object_name = "offers"


class JobOfferDetailView(FormMixin, DetailView):
    model = JobOffer
    template_name = "careers/detail.html"
    context_object_name = "offer"
    form_class = JobOfferEmailForm

    def get_success_url(self):
        return reverse("careers:thanks")

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        allowed_content_types = [
            "application/pdf",
            "application/msword",
            "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        ]

        resume = form.cleaned_data["resume"]
        if resume.content_type not in allowed_content_types:
            raise ValidationError("Content type not supported.")

        name = (
            form.cleaned_data["first_name"]
            if form.cleaned_data["first_name"]
            else form.cleaned_data["email"]
        )
        subject = f"JOB OFFER REPLAY: {name} responded to {self.object.title} offer from {self.object.created}."
        message = (
            f"{form.cleaned_data['email']} {name if form.cleaned_data['first_name'] else ''} sent a resume for {self.object.title} "
            f"job offer in the office at {self.object.location.street} created at {self.object.created}."
        )
        email = form.cleaned_data["email"]

        mail = EmailMessage(subject, message, email, [settings.EMAIL_HOST_USER])
        mail.attach(resume.name, resume.read(), resume.content_type)
        mail.send()
        return super().form_valid(form)


class JobOfferThankYouView(TemplateView):
    template_name = 'careers/thanks.html'
