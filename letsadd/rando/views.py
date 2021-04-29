from django.views.generic import FormView

from .forms import RandomForm


class RandomFormView(FormView):
    form_class = RandomForm
    template_name = 'rando/random_form.html'

    def get(self, request, *args, **kwargs):
        if request.GET:
            form = self.get_form()
            if form.is_valid():
                return self.form_valid(form)
            else:
                return self.form_invalid(form)
        return super().get(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.method == 'GET' and self.request.GET:
            kwargs['data'] = self.request.GET
        return kwargs

    def form_valid(self, form):
        kwargs = {
            'form': form,
            'number': form.generate_number(),
        }
        return self.render_to_response(self.get_context_data(**kwargs))
