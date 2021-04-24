from django.urls import path

from .views import add


app_name = 'add'

urlpatterns = [
    path('', add, name='add_form'),
]
