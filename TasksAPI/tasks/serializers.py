from .models import Tasks
from rest_framework import serializers
from django.utils import timezone

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tasks
        fields='__all__'

        # Perform custom validation 
    def validate(self, data):
        due_date = data.get('due_date')

        if due_date and due_date <= timezone.now():
            raise serializers.ValidationError({'due_date': 'Due date must be in the future.'})

        return data
    
