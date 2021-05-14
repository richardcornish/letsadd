from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import AlphabetizeForm


class AlphabetizeFormView(FormView):
    form_class = AlphabetizeForm
    template_name = 'alphabetize/alphabetize_form.html'
    success_url = reverse_lazy('alphabetize:alphabetize_form')

    def form_valid(self, form):
        initial = {
            'text': form.alphabetize(),
        }
        form = AlphabetizeForm(initial=initial)
        return self.render_to_response(self.get_context_data(form=form))
