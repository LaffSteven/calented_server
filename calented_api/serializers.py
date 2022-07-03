from wsgiref.handlers import format_date_time
from rest_framework import serializers 
from .models import CalEvent

class CalEventSerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    class Meta:
        model = CalEvent # tell django which model to use
        fields = ('id','date', 'title', 'description',) # tell django which fields to include