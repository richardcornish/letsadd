from django.urls import path

from .views import PostDetailView, SearchView


app_name = 'fetch'

urlpatterns = [
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('', SearchView.as_view(), name='search'),
]
