from django.urls import path

from .views import add


urlpatterns = [
    path('', add, name='add_form'),
]
