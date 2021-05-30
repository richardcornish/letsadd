from django.conf import settings
from django.views.generic import FormView

from .forms import SearchForm

PHOTO_MAX_WIDTH = 320


class SearchView(FormView):
    form_class = SearchForm
    template_name = 'geocode/search.html'

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
        query = form.cleaned_data['address']
        kwargs = {
            'query': query,
            'result_list': form.get_results(query),
            'max_width': PHOTO_MAX_WIDTH,
            'google_api_key': settings.GOOGLE_API_KEY,
        }
        return self.render_to_response(self.get_context_data(**kwargs))
