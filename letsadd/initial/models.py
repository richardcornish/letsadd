from django.db import models
from django.urls import reverse


class Profile(models.Model):
    residence = models.CharField(max_length=50)

    def __str__(self):
        return '%s' % self.pk

    def get_absolute_url(self):
        return reverse('initial:profile_detail', args=[str(self.pk)])


class Post(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s' % self.timestamp

    def get_absolute_url(self):
        return reverse('initial:post_detail', args=[str(self.pk)])
