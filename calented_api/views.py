from django.shortcuts import render
from rest_framework import generics
from .serializers import CalEventSerializer
from .models import CalEvent
# Create your views here.


class CalEventList(generics.ListCreateAPIView):
    queryset = CalEvent.objects.all().order_by('date') # tell django how to retrieve all objects from the DB, order by date ascending
    serializer_class = CalEventSerializer # tell django what serializer to use

class CalEventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CalEvent.objects.all().order_by('date')
    serializer_class = CalEventSerializer