from django.db import models
from django.urls import reverse

from .managers import ParkManager


class Park(models.Model):
    name = models.CharField(max_length=254)
    slug = models.SlugField(unique=True)
    location = models.CharField(max_length=254)
    latitude = models.FloatField()
    longitude = models.FloatField()
    established = models.DateField()
    area = models.FloatField(help_text='acres')
    visitors = models.PositiveIntegerField(blank=True, null=True)
    description = models.TextField(blank=True)
    whs = models.BooleanField('World Heritage Site', default=False)
    br = models.BooleanField('Biosphere Reserve', default=False)
    url = models.URLField('URL')

    objects = ParkManager()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('haversine:park_detail', args=[self.slug])
