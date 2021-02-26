from rest_framework import serializers
from .models import Bug

class BugSerializer(serializers.ModelSerializer):
   class Meta:
       model = Bug
       fields = ['name', 'priority', 'details', 'steps', 'operating_system','assignee','resolved']
