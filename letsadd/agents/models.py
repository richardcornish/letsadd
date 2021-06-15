from django.db import models
from django.urls import reverse


class Agent(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('agents:agent_detail', args=[str(self.pk)])


class Invoice(models.Model):
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    invoice_amount = models.DecimalField(decimal_places=2, max_digits=9)

    def __str__(self):
        return '%s' % self.invoice_amount
