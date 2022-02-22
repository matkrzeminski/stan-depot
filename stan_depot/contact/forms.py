from django import forms

from .models import Place


class PlaceCreateForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ["name", "address"]
        help_texts = {
            "name": "E.G. Złote Tarasy",
            "address": "E.G. Złota 59 00-120 Warszawa",
        }


class PlaceUpdateForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = "__all__"
        help_texts = {
            "name": "E.G. Złote Tarasy",
            "address": "E.G. Złota 59, 00-120 Warszawa",
            "street": "E.G. Złota 59",
            "zip_code": "E.G. 00-120",
            "city": "E.G. Warszawa",
            "country": "E.G. Polska",
            "latitude": "E.G. 52.2300795",
            "longitude": "E.G. 21.002446260760067",
        }


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=120, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(required=True, widget=forms.Textarea)
