from django.shortcuts import render

from .forms import SeriesForm


def series(request):
    total = 0
    if request.GET:

        # QueryDict instances (request.GET) are immutable, so make a copy for 
        # the form. We manipulate the form data later for state purposes.
        # https://docs.djangoproject.com/en/3.2/ref/request-response/#querydict-objects
        # https://docs.djangoproject.com/en/3.2/ref/request-response/#django.http.QueryDict.copy
        form = SeriesForm(request.GET.copy())

        if form.is_valid():
            total = form.add_numbers()

            # Mutate the form data's "previous" key to maintain the running 
            # total. This is usually a "no, no" but changing the form data 
            # maintains the state so that upon next form submission, 
            # "previous" contains the total required to correctly compute the 
            # next total. The form's cleaned data can be used to access 
            # values from the last submission as needed.
            # TL;DR: "previous is the new total"
            form.data['previous'] = total

    else:
        form = SeriesForm()
    return render(request, 'series/series_form.html', {
        'form': form,
        'total': total,
    })
