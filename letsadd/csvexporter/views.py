import csv

from django.http import HttpResponse
from django.shortcuts import render

from .forms import CustomerForm
from .models import Customer


def customer_list(request):
    qs = Customer.objects.all()
    if request.GET:
        form = CustomerForm(request.GET)
        if form.is_valid():
            export = form.cleaned_data.pop('export')
            qs = qs.filter(**form.cleaned_data)
            if export:
                response = HttpResponse(content_type='text/csv')
                response['Content-Disposition'] = 'attachment; filename="%s.csv"' % form.cleaned_data['flag']
                writer = csv.writer(response)
                writer.writerow([f.name for f in Customer._meta.get_fields()])
                rows = [writer.writerow(t) for t in qs.values_list()]
                return response
    else:
        form = CustomerForm()
    return render(request, 'csvexporter/customer_list.html', {
        'object_list': qs,
        'form': form,
    })
