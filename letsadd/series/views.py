from django.shortcuts import render

from .forms import SeriesForm


def series(request):
    prev = None
    total = 0
    if request.GET:
        form = SeriesForm(request.GET)
        if form.is_valid():
            prev = form.cleaned_data['prev']
            total = form.add_numbers()
            data = request.GET.copy()
            data.__setitem__('prev', int(request.GET.get('prev')) + int(request.GET.get('num')))
            form = SeriesForm(data)
    else:
        form = SeriesForm()
    return render(request, 'series/series_form.html', {
        'form': form,
        'previous': prev,
        'total': total,
    })
