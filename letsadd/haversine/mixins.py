import json

from django.core import serializers
from django.template.defaultfilters import floatformat


class JsonSingleObjectMixin:

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object:
            context['object_json'] = json.dumps(json.loads(serializers.serialize('json', [self.object], fields=('latitude', 'longitude')))[0]['fields'])
        return context


class JsonMultipleObjectMixin:

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object_list:
            object_list = json.loads(serializers.serialize('json', self.object_list, fields=('name', 'latitude', 'longitude')))
            for obj in object_list:
                qs_object = self.object_list.get(pk=obj['pk'])
                if hasattr(qs_object, 'distance'):  # check for annotated QuerySet
                    obj['fields']['distance'] = floatformat(qs_object.distance, arg='0g')
                obj['fields']['get_absolute_url'] = self.object_list.get(pk=obj['pk']).get_absolute_url()
            context['object_list_json'] = json.dumps([obj['fields'] for obj in object_list])
        return context
