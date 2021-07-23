from django.urls import path

from .views import OrganizeFormView


app_name = 'alphabetize'

urlpatterns = [
    path('', OrganizeFormView.as_view(), name='organize_form'),
]
