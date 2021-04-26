from django.db import models
from django.urls import reverse


class Ceremony(models.Model):
    title = models.CharField(max_length=254)
    year = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ['-year']
        verbose_name_plural = 'ceremonies'

    def __str__(self):
        return '%s' % self.title


class Category(models.Model):
    title = models.CharField(max_length=254)

    class Meta:
        ordering = ['title']
        verbose_name_plural = 'categories'

    def __str__(self):
        return '%s' % self.title


class Nominee(models.Model):
    ceremony = models.ForeignKey(Ceremony, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=254)
    recipient = models.BooleanField(null=True)

    class Meta:
        ordering = ['name', 'ceremony', 'category']

    def __str__(self):
        return '%s' % self.name


class Ballot(models.Model):
    name = models.CharField(max_length=254)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return '%s' % self.name

    def get_absolute_url(self):
        return reverse('oscars:ballot_detail', args=[str(self.pk)])

    def scores(self):
        qs = self.choice_set.all()
        scores = {
            'correct': 0,
            'incorrect': 0,
            'tbd': 0,
            'total': qs.count(),
        }
        for obj in qs:
            if obj.nominee.recipient == True:
                scores['correct'] += 1
            if obj.nominee.recipient == False:
                scores['incorrect'] += 1
            elif obj.nominee.recipient == None:
                scores['tbd'] += 1            
        return scores


class Choice(models.Model):
    ballot = models.ForeignKey(Ballot, on_delete=models.CASCADE)
    nominee = models.ForeignKey(Nominee, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % self.nominee
