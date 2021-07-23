import os

from django import forms

INITIAL_TEXT = 'Superman\n\
Batman\n\
Spider-Man\n\
Superman\n\
\n\
Wonder Woman\n\
Captain America\n\
Wolverine\n\
Wolverine\n\
Green Lantern\n\
Black Panther\n\
The Flash\n\
\n\
\n\
Thor\r\n\
\r\n'


class OrganizeForm(forms.Form):
    ORDER_CHOICES = [
        ('+', 'Ascending (A-Z)'),
        ('-', 'Descending (Z-A)'),
        ('noop', 'Preserve order'),
    ]
    text = forms.CharField(initial=INITIAL_TEXT, strip=False, widget=forms.Textarea(attrs={'placeholder': 'Enter text'}))
    order = forms.ChoiceField(choices=ORDER_CHOICES, initial='+', widget=forms.RadioSelect)
    remove_duplicates = forms.BooleanField(label='Remove duplicates?', initial=True, required=False)
    remove_empty = forms.BooleanField(label='Remove empty lines?', initial=True, required=False, help_text='Note: Even if empty lines are kept, number of empty lines collapses to one if <code>remove duplicates</code> is selected!')

    def get_uniqueified_list(self, iterable):
        # https://stackoverflow.com/questions/480214/how-do-you-remove-duplicates-from-a-list-whilst-preserving-order
        seen = set()
        seen_add = seen.add
        return [x for x in iterable if not (x in seen or seen_add(x))]

    def clean(self):
        cleaned_data = self.cleaned_data
        text = cleaned_data.get('text')
        if text:
            iterable = text.splitlines()

            # Remove duplicates
            if cleaned_data.get('remove_duplicates'):
                iterable = self.get_uniqueified_list(iterable)

            # Remove empty lines
            if cleaned_data.get('remove_empty'):
                iterable = [s for s in iterable if s.strip()]

            # Sort order
            order = cleaned_data.get('order')
            if order == '+':
                reverse = False
            elif order == '-':
                reverse = True
            else:
                reverse = None
            if reverse is not None:
                iterable = sorted(iterable, key=str.casefold, reverse=reverse)

            iterable = os.linesep.join(iterable)
            cleaned_data['text'] = iterable
            return cleaned_data
