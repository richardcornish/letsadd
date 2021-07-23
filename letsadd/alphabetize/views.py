from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import OrganizeForm


class OrganizeFormView(FormView):
    form_class = OrganizeForm
    template_name = 'alphabetize/organize_form.html'
    success_url = reverse_lazy('alphabetize:organize_form')

    def form_valid(self, form):
        initial = form.cleaned_data.copy()
        initial['text'] = form.cleaned_data['text']
        form = self.form_class(initial=initial)
        return self.render_to_response(self.get_context_data(form=form))
