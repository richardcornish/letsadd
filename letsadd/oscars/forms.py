from django import forms

from .models import Ballot, Nominee

WIDGET = forms.RadioSelect

YEAR = 2021


class BallotForm(forms.ModelForm):
    best_picture = forms.ModelChoiceField(widget=WIDGET, queryset=Nominee.objects.filter(
        ceremony__year=YEAR, category__title='Best Picture'))
    best_director = forms.ModelChoiceField(widget=WIDGET, queryset=Nominee.objects.filter(
        ceremony__year=YEAR, category__title='Best Director'))
    best_actor = forms.ModelChoiceField(widget=WIDGET, queryset=Nominee.objects.filter(
        ceremony__year=YEAR, category__title='Best Actor'))
    best_actress = forms.ModelChoiceField(widget=WIDGET, queryset=Nominee.objects.filter(
        ceremony__year=YEAR, category__title='Best Actress'))
    best_supporting_actor = forms.ModelChoiceField(widget=WIDGET, queryset=Nominee.objects.filter(
        ceremony__year=YEAR, category__title='Best Supporting Actor'))
    best_supporting_actress = forms.ModelChoiceField(widget=WIDGET, queryset=Nominee.objects.filter(
        ceremony__year=YEAR, category__title='Best Supporting Actress'))
    best_original_screenplay = forms.ModelChoiceField(widget=WIDGET, queryset=Nominee.objects.filter(
        ceremony__year=YEAR, category__title='Best Original Screenplay'))
    best_adapted_screenplay = forms.ModelChoiceField(widget=WIDGET, queryset=Nominee.objects.filter(
        ceremony__year=YEAR, category__title='Best Adapted Screenplay'))
    best_animated_feature_film = forms.ModelChoiceField(widget=WIDGET, queryset=Nominee.objects.filter(
        ceremony__year=YEAR, category__title='Best Animated Feature Film'))
    best_international_feature_film = forms.ModelChoiceField(widget=WIDGET, queryset=Nominee.objects.filter(
        ceremony__year=YEAR, category__title='Best International Feature Film'))
    best_documentary_feature = forms.ModelChoiceField(widget=WIDGET, queryset=Nominee.objects.filter(
        ceremony__year=YEAR, category__title='Best Documentary Feature'))
    best_documentary_short_subject = forms.ModelChoiceField(widget=WIDGET, queryset=Nominee.objects.filter(
        ceremony__year=YEAR, category__title='Best Documentary Short Subject'))
    best_live_action_short_film = forms.ModelChoiceField(widget=WIDGET, queryset=Nominee.objects.filter(
        ceremony__year=YEAR, category__title='Best Live Action Short Film'))
    best_animated_short_film = forms.ModelChoiceField(widget=WIDGET, queryset=Nominee.objects.filter(
        ceremony__year=YEAR, category__title='Best Animated Short Film'))
    best_original_score = forms.ModelChoiceField(widget=WIDGET, queryset=Nominee.objects.filter(
        ceremony__year=YEAR, category__title='Best Original Score'))
    best_original_song = forms.ModelChoiceField(widget=WIDGET, queryset=Nominee.objects.filter(
        ceremony__year=YEAR, category__title='Best Original Song'))
    best_sound = forms.ModelChoiceField(widget=WIDGET, queryset=Nominee.objects.filter(
        ceremony__year=YEAR, category__title='Best Sound'))
    best_production_design = forms.ModelChoiceField(widget=WIDGET, queryset=Nominee.objects.filter(
        ceremony__year=YEAR, category__title='Best Production Design'))
    best_cinematography = forms.ModelChoiceField(widget=WIDGET, queryset=Nominee.objects.filter(
        ceremony__year=YEAR, category__title='Best Cinematography'))
    best_makeup_and_hairstyling = forms.ModelChoiceField(widget=WIDGET, queryset=Nominee.objects.filter(
        ceremony__year=YEAR, category__title='Best Makeup and Hairstyling'))
    best_costume_design = forms.ModelChoiceField(widget=WIDGET, queryset=Nominee.objects.filter(
        ceremony__year=YEAR, category__title='Best Costume Design'))
    best_film_editing = forms.ModelChoiceField(widget=WIDGET, queryset=Nominee.objects.filter(
        ceremony__year=YEAR, category__title='Best Film Editing'))
    best_visual_effects = forms.ModelChoiceField(widget=WIDGET, queryset=Nominee.objects.filter(
        ceremony__year=YEAR, category__title='Best Visual Effects'))

    class Meta:
        model = Ballot
        fields = [
            'name',
            'best_picture',
            'best_director',
            'best_actor',
            'best_actress',
            'best_supporting_actor',
            'best_supporting_actress',
            'best_original_screenplay',
            'best_adapted_screenplay',
            'best_animated_feature_film',
            'best_international_feature_film',
            'best_documentary_feature',
            'best_documentary_short_subject',
            'best_live_action_short_film',
            'best_animated_short_film',
            'best_original_score',
            'best_original_song',
            'best_sound',
            'best_production_design',
            'best_cinematography',
            'best_makeup_and_hairstyling',
            'best_costume_design',
            'best_film_editing',
            'best_visual_effects',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''
