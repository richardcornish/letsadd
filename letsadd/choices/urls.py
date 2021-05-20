from django.urls import path

from .views import BotCreateView, BotDetailView, BotListView, BotUpdateView


app_name = 'choices'

urlpatterns = [
    path('<int:pk>/edit/', BotUpdateView.as_view(), name='bot_update'),
    path('<int:pk>/', BotDetailView.as_view(), name='bot_detail'),
    path('add/', BotCreateView.as_view(), name='bot_create'),
    path('', BotListView.as_view(), name='bot_list'),
]
