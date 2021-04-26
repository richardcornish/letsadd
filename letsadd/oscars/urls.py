from django.urls import path

from .views import BallotCreateView, BallotDetailView


app_name = 'oscars'

urlpatterns = [
    path('ballots/<int:pk>/', BallotDetailView.as_view(), name='ballot_detail'),
    path('', BallotCreateView.as_view(), name='ballot_create'),
]
