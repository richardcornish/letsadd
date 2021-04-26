from django.views.generic import CreateView, DetailView

from .forms import BallotForm
from .models import Ballot, Choice, Nominee


class BallotCreateView(CreateView):
    model = Ballot
    form_class = BallotForm

    def form_valid(self, form):
        response = super().form_valid(form)
        for key in form.cleaned_data:
            ballot = form.instance
            nominee = form.cleaned_data[key]
            if isinstance(nominee, Nominee):
                Choice.objects.create(ballot=ballot, nominee=nominee)
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ballot_list'] = Ballot.objects.all()
        return context


class BallotDetailView(DetailView):
    model = Ballot
