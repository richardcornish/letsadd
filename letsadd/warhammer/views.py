from urllib.parse import urlparse, parse_qs

from django.shortcuts import render
from django.views.generic import FormView

from .forms import ChapterForm
from .utils.choices import generate_chapter, generate_human


class ChapterFormView(FormView):
    form_class = ChapterForm
    template_name = 'warhammer/chapter_form.html'

    def get(self, request, *args, **kwargs):
        if request.GET:
            form = self.get_form()
            if form.is_valid():
                return self.form_valid(form)
            else:
                return self.form_invalid(form)
        return super().get(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.method == 'GET' and self.request.GET:
            kwargs['data'] = self.request.GET.copy()
        return kwargs

    def form_valid(self, form):
        if 'submit_chapter' in self.request.GET:
            form.data['chapter'] = form.generate_chapter()
        if 'submit_name' in self.request.GET:
            form.data['name'] = form.generate_name()
        return self.render_to_response(self.get_context_data(form=form))


def chapter_form(request):

    print(request.META['QUERY_STRING'])
    print(request.build_absolute_uri())
    pr = urlparse(request.build_absolute_uri())
    query = parse_qs(pr.query)
    print(query)

    if request.GET:

        print(request.GET)

        form = ChapterForm(request.GET.copy())
        if form.is_valid():
            print(form.cleaned_data)

        if 'chapter' in request.GET or 'chapter' in query:
            chapter = request.GET.get('chapter')
            next_chapter = generate_chapter()
            human = query.get('human', '')
            next_human = generate_human()

        if 'human' in request.GET or 'human' in query:
            chapter = query.get('chapter', '')
            next_chapter = generate_chapter()
            human = request.GET.get('human')
            next_human = generate_human()

        # pr = urlparse(request.build_absolute_uri())
        # query = parse_qs(pr.query)
        # if 'name' in query:
        #     data['name'] = query.get('name')[0]
        # if 'chapter' in query:
        #     data['chapter'] = query.get('chapter')[0]

        # chapter = form.generate_chapter()
        # name = form.generate_name()

    else:
        chapter = ''
        human = ''
        next_chapter = generate_chapter()
        next_human = generate_human()
        form = ChapterForm()
    return render(request, 'warhammer/chapter_form.html', {
        'form': form,
        'chapter': chapter,
        'human': human,
        'next_chapter': next_chapter,
        'next_human': next_human,        
    })



def chapter_form(request):
    print(request.get_full_path())
    return render(request, 'warhammer/chapter_form.html', {})










