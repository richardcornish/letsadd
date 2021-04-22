from django.urls import path

from .views import ClickCreateView, ClickDeleteView


urlpatterns = [
    path('delete/', ClickDeleteView.as_view(), name='click_delete'),
    path('', ClickCreateView.as_view(), name='click_create'),
]
