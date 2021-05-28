from django.urls import path

from .views import ProfileCreateView, ProfileDetailView, ProfileListView, ProfileUpdateView


app_name = 'twilidator'

urlpatterns = [
    path('<int:pk>/edit/', ProfileUpdateView.as_view(), name='profile_update'),
    path('<int:pk>/', ProfileDetailView.as_view(), name='profile_detail'),
    path('add/', ProfileCreateView.as_view(), name='profile_create'),
    path('', ProfileListView.as_view(), name='profile_list'),
]
