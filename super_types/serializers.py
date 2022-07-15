from rest_framework import serializers
from .models import SuperType
class SuperTypeSerializer(serializers.SuperTypeSerializer):
    class Meta:
        model = SuperType
        fields = ['type']

