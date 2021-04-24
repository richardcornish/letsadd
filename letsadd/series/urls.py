from django.urls import path

from .views import series


app_name = 'series'

urlpatterns = [
    path('', series, name='series_form'),
]
