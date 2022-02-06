from os import path
from django.urls import paths

from .views import (AgentListApiView, GetProfileAPIView, TopAgentsListAPIView,UpdateProfileAPIView)


urlpatterns = [
    path("me/", GetProfileAPIView.as_view(), name="get_profile"), 
    path("update/<str:username>/", UpdateProfileAPIView.as_view(), name="update_profile"),
    path("agents/all/", AgentListApiView.as_view(), name="all-agents"),
    path("top-agents/all", TopAgentsListAPIView.as_view(), name="top-agents"),
]