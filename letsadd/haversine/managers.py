from django.db import models
from django.db.models import F
from django.db.models.functions import ATan2, Cos, Power, Radians, Sin, Sqrt

EARTH_RADIUS = 6371000  # meters
METERS_IN_MILE = 1609.344  # meters


class ParkQuerySet(models.QuerySet):
    """
    https://en.wikipedia.org/wiki/Earth_radius
    https://en.wikipedia.org/wiki/Haversine_formula
    https://www.movable-type.co.uk/scripts/latlong.html
    """
    def annotate_distance(self, point):

        lat_1 = point['latitude']
        lon_1 = point['longitude']
        lat_2 = F('latitude')
        lon_2 = F('longitude')

        phi_1 = Radians(lat_1)
        phi_2 = Radians(lat_2)
        delta_phi = Radians(lat_2 - lat_1)
        delta_lambda = Radians(lon_2 - lon_1)

        a = Power(Sin(delta_phi / 2), 2) +\
            Cos(phi_1) * Cos(phi_2) *\
            Power(Sin(delta_lambda / 2), 2)

        c = 2 * ATan2(Sqrt(a), Sqrt(1 - a))

        r_mi = EARTH_RADIUS / METERS_IN_MILE
        r_km = EARTH_RADIUS / 1000

        d_m = c * r_mi  # miles
        d_km = c * r_km  # kilometers

        return self.exclude(latitude=None).exclude(longitude=None).annotate(distance_m=d_m, distance_km=d_km)


class ParkManager(models.Manager):
    def get_queryset(self):
        return ParkQuerySet(self.model, using=self._db)  # important

    def annotate_distance(self, point):
        return self.get_queryset().annotate_distance(point)
