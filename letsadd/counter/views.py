import json

from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, View

from .models import Click


class ClickCreateView(CreateView):
    model = Click
    fields = []
    success_url = reverse_lazy('counter:click_create')

    def request_is_ajax(self):
        return self.request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request_is_ajax():
            data = json.loads(serializers.serialize('json', [self.object]))[0]
            return JsonResponse(data)
        return response

    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request_is_ajax():
            return JsonResponse(form.errors, status=400)
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['click_list'] = Click.objects.all()
        return context


class ClickDeleteView(View):

    def post(self, *args, **kwargs):
        Click.objects.all().delete()
        return redirect(reverse('counter:click_create'))
