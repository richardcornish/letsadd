from django.db.models import Count
from django.views.generic import ListView

from .models import Visit


class VisitListView(ListView):
    model = Visit

    def get(self, *args, **kwargs):
        obj = Visit.objects.create()
        return super().get(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['aggregate'] = super().get_queryset().aggregate(Count('pk'))
        return context
