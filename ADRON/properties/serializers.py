from rest_framework import serializers
from .models import Properties

class PropertySerializers(serializers.ModelSerializer):
    class Meta:
        model = Properties
        fields = '__all__'