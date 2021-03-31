from django.shortcuts import render

from .forms import AddForm


def home(request):
    result = None
    if request.GET:
        form = AddForm(request.GET)
        if form.is_valid():
            result = form.add_numbers()
    else:
        form = AddForm()
    return render(request, 'home.html', {
        'form': form,
        'result': result,
    })
