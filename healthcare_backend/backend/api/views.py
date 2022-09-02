from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from . models import *
from .serializers import diseaseSerializer, symptomSerializer
# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    routes=[
        {
            'endpoint':'',
            'method':'GET',
            'status':True,
            'description': "get all the routes"
        },
    ]
    return Response(routes)

# for diseases
@api_view(['GET'])
def viewDisease(request):
    diseases= Disease.objects.all()
    serializers = diseaseSerializer(diseases, many=True)
    return Response(serializers.data)

@api_view(['POST'])
def createDisease(request):
    data=request.data
    disease=Disease.objects.create(name=data['name'])
    serializer = diseaseSerializer(disease, many=False)
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteDisease(request,pk):
    disease=Disease.objects.get(id=pk)
    disease.delete()
    return Response('disease was deleted')

# for symptoms

@api_view(['GET'])
def viewSymptom(request):
    symptoms= Symptom.objects.all()
    serializers = symptomSerializer(symptoms, many=True)
    return Response(serializers.data)

@api_view(['POST'])
def createSymptom(request):
    data=request.data
    symptom=Symptom.objects.create(body=data['body'])
    serializer = symptomSerializer(symptom, many=False)
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteSymptom(request,pk):
    symptom=Symptom.objects.get(id=pk)
    symptom.delete()
    return Response('symptom was deleted')
