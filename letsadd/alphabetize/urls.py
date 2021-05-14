from django.urls import path

from .views import AlphabetizeFormView


app_name = 'alphabetize'

urlpatterns = [
    path('', AlphabetizeFormView.as_view(), name='alphabetize_form'),
]
