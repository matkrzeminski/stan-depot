from django.db import models
from django.urls import reverse

from .utils.process_geocoder_data import process_geocoder_data


class Place(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    street = models.CharField(max_length=255, blank=True)
    zip_code = models.CharField(max_length=6, blank=True)
    city = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)
    latitude = models.CharField(max_length=255, blank=True)
    longitude = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.name} at {self.address}"

    def get_absolute_url(self):
        """Return absolute URL to the Stan Depot Contact page."""
        return reverse("contact:home")

    def save(self, *args, **kwargs):
        """Gets all needed information for the Place object
        based on the value provided in the address field and saves it."""
        if self._state.adding:
            import geocoder

            g = geocoder.osm(  # Valid results for both street and popular place
                self.address  # E.G. plac Defilad 1, 00-901 Warszawa and Pałac Kultury i Nauki
            )

            data = process_geocoder_data(g)

            if data:
                self.latitude = data.get("latitude")
                self.longitude = data.get("longitude")
                self.street = data.get("street")
                self.city = data.get("city")
                self.zip_code = data.get("zip_code")
                self.country = data.get("country")

        super().save(*args, **kwargs)
