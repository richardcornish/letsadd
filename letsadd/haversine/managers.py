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
    def annotate_distance(self, point, units=None):

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

        if units == 'mi':
            r = EARTH_RADIUS / METERS_IN_MILE
        elif units == 'km':
            r = EARTH_RADIUS / 1000
        else:
            r = EARTH_RADIUS / METERS_IN_MILE  # miles

        d = c * r

        return self.exclude(latitude=None).exclude(longitude=None).annotate(distance=d)


class ParkManager(models.Manager):
    def get_queryset(self):
        return ParkQuerySet(self.model, using=self._db)  # important

    def annotate_distance(self, point, units=None):
        return self.get_queryset().annotate_distance(point, units=units)
