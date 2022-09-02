
from dataclasses import field

from rest_framework.serializers import ModelSerializer

from .models import Disease,  Symptom

class diseaseSerializer(ModelSerializer):
    class Meta:
        model= Disease
        fields='__all__'
class symptomSerializer(ModelSerializer):
    class Meta:
        model= Symptom
        fields='__all__'