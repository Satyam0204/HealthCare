from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

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
