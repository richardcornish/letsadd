import json

from django.conf import settings
from django.core import serializers
from django.urls import reverse
from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormMixin

from .forms import SearchForm
from .mixins import JsonMultipleObjectMixin, JsonSingleObjectMixin
from .models import Park


class ParkListView(JsonMultipleObjectMixin, FormMixin, ListView):
    model = Park
    form_class = SearchForm

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
        kwargs = {}
        kwargs.update(form.cleaned_data)
        kwargs.update({'%s_json' % f: json.dumps(form.cleaned_data[f]) for f in form.cleaned_data})
        point = form.get_point(form.cleaned_data['address'])
        if point:
            kwargs.update({
                'point': point,
                'point_json': json.dumps(point),
            })
            self.object_list = super().get_queryset()\
                .annotate_distance(point, units=form.cleaned_data['units'])\
                .order_by('distance').filter(distance__lte=form.cleaned_data['radius'])
        return self.render_to_response(self.get_context_data(**kwargs))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['google_api_key'] = settings.GOOGLE_API_KEY
        return context


class ParkDetailView(JsonSingleObjectMixin, DetailView):
    model = Park

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['google_api_key'] = settings.GOOGLE_API_KEY
        context['previous'] = self.request.META.get('HTTP_REFERER', reverse('haversine:park_list'))
        return context
