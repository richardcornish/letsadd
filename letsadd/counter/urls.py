from django.urls import path

from .views import VisitListView


app_name = 'counter'

urlpatterns = [
    path('', VisitListView.as_view(), name='visit_list'),
]
