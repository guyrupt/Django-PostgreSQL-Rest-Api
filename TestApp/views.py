from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse

from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import *
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
    
    company_data = {}
    company_data['company_name'] = data['company.name']
    company_data['icon_url'] = data['company.icon']
    company, _ = Company.objects.get_or_create(company_data)

    location, _ = Location.objects.get_or_create(location_name=data['location'])
    location.company.add(company)

    tag, _ = Tag.objects.get_or_create(tag_name=data['tag'])
    tag.company.add(company)

    level, _ = Level.objects.get_or_create(level_name=data['level'], 
    company=company)

    gender, _ = Gender.objects.get_or_create(gender=data['gender'])
    race, _ = Race.objects.get_or_create(race=data['Race'])
    academic_level, _ = Acad_level.objects.get_or_create(acad_level=data['Academic Level'])
    
    dbo = lambda x: True if x else False
    remote = dbo(data['Remote'])

    employee = Employee.objects.create(
        timestamp=data['timestamp'],
        yearsofexperience = data['yearsofexperience'],
        yearsatcompany = data['yearsatcompany'],
        totalyearlycompensation = data['totalyearlycompensation'],
        base_salary = data['basesalary'],
        stockgrantvalue = data['stockgrantvalue'],
        bonus = data['bonus'], 
        remote = remote,
        location = location,
        tag = tag,
        level = level,
        gender = gender,
        race = race,
        academic_level = academic_level
    )

    return Response('nice', status=status.HTTP_201_CREATED)