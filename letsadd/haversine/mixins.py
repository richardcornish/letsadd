import json

from django.core import serializers
from django.template.defaultfilters import floatformat


class JsonSingleObjectMixin:
    json_suffix = '_json'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'object' in context:
            object_json = json.dumps(json.loads(serializers.serialize('json', [context['object']], fields=('latitude', 'longitude')))[0]['fields'])
            context['object%s' % self.json_suffix] = object_json
            context_object_name = self.get_context_object_name(context['object'])
            if context_object_name:
                context['%s%s' % (context_object_name, self.json_suffix)] = object_json
        return context


class JsonMultipleObjectMixin:
    json_suffix = '_json'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'object_list' in context:
            object_list = json.loads(serializers.serialize('json', context['object_list'], fields=('name', 'latitude', 'longitude')))
            for obj in object_list:
                obj_qs = context['object_list'].get(pk=obj['pk'])
                if hasattr(obj_qs, 'distance'):  # check for annotated QuerySet
                    obj['fields']['distance'] = floatformat(obj_qs.distance, arg='0g')
                obj['fields']['get_absolute_url'] = obj_qs.get_absolute_url()
            object_list_json = json.dumps([obj['fields'] for obj in object_list])
            context['object_list%s' % self.json_suffix] = object_list_json
            context_object_name = self.get_context_object_name(context['object_list'])
            if context_object_name:
                context['%s%s' % (context_object_name, self.json_suffix)] = object_list_json
        return context
