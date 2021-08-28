from django.urls import path
from .views import *

urlpatterns = [
    path("",RunView.as_view(),name="runs"),
    path("<pk>",RunDetail.as_view(),name="run_details"),
    path("stamps/<pk>",RunStampView.as_view(),name="stamps")
]
