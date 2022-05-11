from django.db import models


class Visit(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return '%s' % self.timestamp
