from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse

from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import *
from .serializers import * 
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'message':'not ready yet',
    }
    return Response(api_urls)

# timestamp	level	totalyearlycompensation	location	yearsofexperience	yearsatcompany	tag	basesalary	stockgrantvalue	bonus	gender	company.name	company.icon	company.registered	Remote	Academic Level	Race
@api_view(['POST'])
def addInstance(request):
    data = JSONParser().parse(request)
    print(type(data))
    return Response(data , status=status.HTTP_201_CREATED)