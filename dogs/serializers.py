from rest_framework import serializers
from .models import Dog

class DogSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','user','name','description','created_at')
        model = Dog