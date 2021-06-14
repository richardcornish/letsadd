from django.db import models
from django.db.models import F
from django.db.models.functions import ASin, Cos, Power, Radians, Sin, Sqrt

EARTH_RADIUS = 6371000  # meters

METERS_IN = {
    'mi': 1609.344,  # meters
    'km': 1000,  # meters
}

DEFAULT_UNITS = 'mi'  # miles


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

        c = 2 * ASin(Sqrt(a))

        units = DEFAULT_UNITS if units is None else units

        r = EARTH_RADIUS / METERS_IN[units]

        d = c * r

        return self.exclude(latitude=None).exclude(longitude=None).annotate(distance=d)
