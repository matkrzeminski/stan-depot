from django import forms
from django.core.validators import FileExtensionValidator


class JobOfferEmailForm(forms.Form):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=50, required=False)
    resume = forms.FileField(
        required=True,
        help_text="Allowed extensions are: pdf, doc, docx.",
        validators=[FileExtensionValidator(allowed_extensions=["pdf", "doc", "docx"])],
    )
