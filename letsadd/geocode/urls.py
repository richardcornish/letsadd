from django.urls import path

from .views import SearchView


app_name = 'geocode'

urlpatterns = [
    path('', SearchView.as_view(), name='search'),
]
