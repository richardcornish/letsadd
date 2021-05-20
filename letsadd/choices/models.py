from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Bot(models.Model):
    SITE_SUPPORTED_CHOICES = [
        ('Adidas', 'Adidas'),
        ('Shopify', 'Shopify'),
        ('Supreme', 'Supreme'),
        ('Footsites', 'Footsites'),
        ('YeezySupply', 'YeezySupply'),
        ('Mesh', 'Mesh'),
        ('AIO', 'AIO'),
    ]
    name = models.CharField(max_length=20)
    site_supported = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50, unique=True, blank=True)
    is_approved = models.BooleanField(default=False, null=True)

    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return '%s, %s' % (self.name, self.is_approved)

    def save(self, *args, **kwargs):
        if not self.pk and not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('choices:bot_detail', args=[str(self.pk)])

    def site_supported_list(self):
        return self.site_supported.split(', ')
