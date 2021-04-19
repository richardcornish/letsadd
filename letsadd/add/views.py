from django.shortcuts import render

from .forms import AddForm


def add(request):
    total = 0
    if request.GET:
        form = AddForm(request.GET)
        if form.is_valid():
            total = form.add_numbers()
    else:
        form = AddForm()
    return render(request, 'add/add_form.html', {
        'form': form,
        'total': total,
    })
