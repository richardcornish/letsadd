from django.db.models import Sum
from django.views.generic import DetailView, ListView

from .models import Agent


class AgentDetailView(DetailView):
    model = Agent

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['aggregate'] = self.object.invoice_set.aggregate(Sum('invoice_amount'))
        return context


class AgentListView(ListView):

    def get_queryset(self):
        return Agent.objects.prefetch_related('invoice_set').annotate(Sum('invoice__invoice_amount'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['aggregate'] = self.get_queryset().aggregate(Sum('invoice__invoice_amount'))
        return context
