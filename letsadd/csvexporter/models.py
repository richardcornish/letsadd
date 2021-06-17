from django.db import models


class Customer(models.Model):
    FLAG_CHOICES = [
        ('example', 'example'),
        ('Electoral', 'Electoral'),
        ('Existing Clients', 'Existing Clients'),
        ('Lapsed', 'Lapsed'),
        ('test', 'test'),
        ('WebOffer', 'WebOffer'),
    ]
    forename = models.CharField(max_length=120)
    surname = models.CharField(max_length=120)
    email = models.EmailField(max_length=120, blank=True)
    company_name = models.CharField(max_length=100, blank=True)
    building_name = models.CharField(max_length=100, blank=True)
    street_name = models.CharField(max_length=100, blank=True)
    locality = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=20, blank=True)
    postcode = models.CharField(max_length=8, blank=True)
    flag = models.CharField(max_length=100, choices=FLAG_CHOICES, default='example')

    class Meta:
        ordering = [
            'company_name',
        ]

    def __str__(self):
        return self.company_name
