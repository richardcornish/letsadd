from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .forms import BotForm
from .models import Bot


class BotDetailView(DetailView):
    model = Bot


class BotListView(ListView):
    model = Bot


class BotCreateView(CreateView):
    model = Bot
    form_class = BotForm


class BotUpdateView(UpdateView):
    model = Bot
    form_class = BotForm

    def get_initial(self):
        initial = super().get_initial()
        initial['site_supported'] = self.object.site_supported.split(', ')
        return initial
