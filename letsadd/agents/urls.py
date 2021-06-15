from django.urls import path

from .views import AgentDetailView, AgentListView, agent_detail, agent_list


app_name = 'agents'

urlpatterns = [
    # path('<int:pk>', AgentDetailView.as_view(), name='agent_detail'),
    # path('', AgentListView.as_view(), name='agent_list'),
    path('<int:pk>', agent_detail, name='agent_detail'),
    path('', agent_list, name='agent_list'),
]
