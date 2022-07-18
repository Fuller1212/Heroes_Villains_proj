
from rest_framework import serializers
from .models import Super

class SuperSerializer(serializers.SuperSerializer):
    class Meta:
        model = Super
        fields = ['name', 'alter_ego', 'primary_ability', 'second_ability','catchphrase', 'super_style', 'super_style_id']
        depth = 1
    super_style_id = serializers.IntegerField(write_only = True)