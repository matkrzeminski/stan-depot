from django.db import models
from django.urls import reverse


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
        return f"{self.name} {self.address}"

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

            try:
                address = g.json["raw"]["address"]
                self.latitude = g.json["raw"]["lat"]
                self.longitude = g.json["raw"]["lon"]
            except TypeError:
                return super().save(*args, **kwargs)

            try:
                self.street = address["street"]
            except KeyError:
                try:
                    self.street = address["road"]
                except KeyError:
                    self.street = ""
            else:
                try:
                    self.street += f" {address['house_number']}"
                except KeyError:
                    pass

            try:
                self.city = address["city"]
            except KeyError:
                self.city = address["county"]

            self.zip_code = address["postcode"]
            self.country = address["country"]

        super().save(*args, **kwargs)
