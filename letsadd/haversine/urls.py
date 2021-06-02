from django.urls import path

from .views import ParkDetailView, ParkListView


app_name = 'haversine'

urlpatterns = [
    path('<slug>/', ParkDetailView.as_view(), name='park_detail'),
    path('', ParkListView.as_view(), name='park_list'),
]
