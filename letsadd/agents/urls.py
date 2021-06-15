from django.urls import path

from .views import AgentDetailView, AgentListView


app_name = 'agents'

urlpatterns = [
    path('<int:pk>', AgentDetailView.as_view(), name='agent_detail'),
    path('', AgentListView.as_view(), name='agent_list'),
]
