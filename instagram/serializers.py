from .models import Instagram
from rest_framework import serializers

class InstagramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instagram
        fields = '__all__'