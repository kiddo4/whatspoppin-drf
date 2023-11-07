from rest_framework import serializers
from .models import Pop


# the pop serializer
class PopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pop
        fields = ['id', 'text', 'created_at']
