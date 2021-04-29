from django.urls import path

from .views import RandomFormView


app_name = 'rando'

urlpatterns = [
    path('', RandomFormView.as_view(), name='random_form'),
]
