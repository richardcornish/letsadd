from django.db import models
from django.urls import reverse


class Profile(models.Model):
    twitter_url = models.URLField('twitter URL')

    def __str__(self):
        return '%s' % self.twitter_url

    def get_absolute_url(self):
        return reverse('twilidator:profile_detail', args=[str(self.pk)])
