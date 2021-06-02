from django.urls import reverse
from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormMixin

from .forms import SearchForm
from .models import Park


class ParkListView(FormMixin, ListView):
    model = Park
    form_class = SearchForm
    template_name = 'haversine/search.html'

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        if request.GET:
            form = self.get_form()
            if form.is_valid():
                return self.form_valid(form)
            else:
                return self.form_invalid(form)
        return response

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.method == 'GET' and self.request.GET:
            kwargs['data'] = self.request.GET
        return kwargs

    def form_valid(self, form):
        kwargs = {
            'query': form.cleaned_data['address'],
            'radius': form.cleaned_data['radius'],
        }
        point = form.get_point(kwargs['query'])
        if point:
            kwargs['point'] = point
            kwargs['object_list'] = super().get_queryset().annotate_distance(point).order_by('distance_m').filter(distance_m__lte=kwargs['radius'])
        return self.render_to_response(self.get_context_data(**kwargs))


class ParkDetailView(DetailView):
    model = Park

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['previous'] = self.request.META.get('HTTP_REFERER', reverse('haversine:park_list'))
        return context
