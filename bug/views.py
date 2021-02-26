# from django.shortcuts import render
from rest_framework import generics
from .serializers import BugSerializer
from .models import Bug

class BugList(generics.ListCreateAPIView):
    queryset = Bug.objects.all()
    serializer_class = BugSerializer

class BugDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bug.objects.all()
    serializer_class = BugSerializer
