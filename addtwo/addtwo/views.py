from django.shortcuts import render

from .forms import AddForm


def home(request):
    result = None
    if request.GET:
        form = AddForm(request.GET)
        if form.is_valid():
            num_one = form.cleaned_data['num_one']
            num_two = form.cleaned_data['num_two']
            result = num_one + num_two
    else:
        form = AddForm()
    return render(request, 'home.html', {
        'form': form,
        'result': result,
    })
