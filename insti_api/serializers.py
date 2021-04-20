from rest_framework import serializers
from institutions.models import University


class UnivSerializers(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = '__all__'