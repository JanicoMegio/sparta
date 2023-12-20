from rest_framework import serializers
from App.models import CustomerData

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerData
        fields = '__all__'