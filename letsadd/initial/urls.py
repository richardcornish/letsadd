from django.urls import path

from .views import post_create, PostDetailView, ProfileDetailView


app_name = 'initial'

urlpatterns = [
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('profiles/<int:pk>/', ProfileDetailView.as_view(), name='profile_detail'),
    path('', post_create, name='post_create'),
]
