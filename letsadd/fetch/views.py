import json

from django.core import serializers
from django.http import JsonResponse
from django.views.generic import DetailView, FormView

from .forms import SearchForm
from .models import Post


class SearchView(FormView):
    form_class = SearchForm
    template_name = 'fetch/search.html'

    def request_is_ajax(self):
        return self.request.headers.get('X-Requested-With') == 'XMLHttpRequest'

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
        query = form.cleaned_data['q']
        queryset = form.get_results(query)
        kwargs = {
            'query': query,
            'object_list': queryset,
        }
        if self.request_is_ajax():
            object_list = json.loads(serializers.serialize('json', queryset, fields=('title', 'content', 'image')))

            # Hack the URL in. This is ugly.
            for obj in object_list:
                obj['fields']['get_absolute_url'] = queryset.get(pk=obj['pk']).get_absolute_url()
            kwargs['object_list'] = object_list

            return JsonResponse(kwargs)
        return self.render_to_response(self.get_context_data(**kwargs))

    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request_is_ajax():
            kwargs = {
                'errors': form.errors,
            }
            return JsonResponse(kwargs, status=400)
        return response


class PostDetailView(DetailView):
    model = Post
