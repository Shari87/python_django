from rest_framework import serializers
from .models import Dog


class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = ('id','env','tests','name', 'age', 'breed', 'color', 'created_at', 'started_at','finished_at','status')