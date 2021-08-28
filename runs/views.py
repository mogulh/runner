from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics

# Create your views here.

class RunView(generics.ListCreateAPIView):
    queryset = Run.objects.all()
    serializer_class = RunSerializer


class RunDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Run.objects.all()
    serializer_class = RunSerializer


class RunStampView(generics.ListCreateAPIView):
    def get_queryset(self):
        run_id = self.kwargs["pk"]
        run = Run.objects.get(pk=run_id)
        return run.stamps.all()
    serializer_class = RunStampSerializer