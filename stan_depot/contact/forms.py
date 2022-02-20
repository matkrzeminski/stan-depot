from django.forms import ModelForm

from .models import Place


class PlaceCreateForm(ModelForm):
    class Meta:
        model = Place
        fields = ["name", "address"]
        help_texts = {
            "name": "E.G. Złote Tarasy",
            "address": "E.G. Złota 59 00-120 Warszawa",
        }


class PlaceUpdateForm(ModelForm):
    class Meta:
        model = Place
        fields = "__all__"
        help_texts = {
            "name": "E.G. Złote Tarasy",
            "address": "E.G. Złota 59 00-120 Warszawa",
            "street": "E.G. Złota 59",
            "zip_code": "E.G. 00-120",
            "city": "E.G. Warszawa",
            "country": "E.G. Polska",
            "latitude": "E.G. 52.2300795",
            "longitude": "E.G. 21.002446260760067",
        }
