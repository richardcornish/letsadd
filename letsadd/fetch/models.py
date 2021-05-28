from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(blank=True)

    def __str__(self):
        return '%s' % self.title

    def get_absolute_url(self):
        return reverse('fetch:post_detail', args=[str(self.pk)])
