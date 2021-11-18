from django.db.models import Avg
from django.forms import model_to_dict
from django.http import response
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from django.db.models.query import EmptyQuerySet

from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import *


# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'message': 'not ready yet',
    }
    return Response(api_urls)


# All data is inserted to database using this API, check ./database/database.ipynb for data
@api_view(['POST'])
def addInstance(request):
    data = JSONParser().parse(request)

    company, _ = Company.objects.get_or_create(company_name=data['company.name'],
                                               icon_url=data['company.icon'])

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
        yearsofexperience=data['yearsofexperience'],
        yearsatcompany=data['yearsatcompany'],
        totalyearlycompensation=data['totalyearlycompensation'],
        base_salary=data['basesalary'],
        stockgrantvalue=data['stockgrantvalue'],
        bonus=data['bonus'],
        remote=remote,
        location=location,
        tag=tag,
        level=level,
        gender=gender,
        race=race,
        academic_level=academic_level
    )

    return Response('nice', status=status.HTTP_201_CREATED)


# 1st API /location/<loc>
# To search places in U.S., type in USPS Abbreviation. In other countries type in country name.
@api_view(['GET'])
def loc_search(request, loc):
    location = Location.objects.filter(location_name__iendswith=loc)
    employees = Employee.objects.none()
    for l in location.iterator():
        employees |= l.employee_set.select_related('level__company', 'tag',
                                                   'level', 'gender', 'race', 'academic_level')
    employees = employees.order_by('-totalyearlycompensation')
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def companies(request):
    company_list = Company.objects.all().order_by('company_name')
    serializer = CompanySerializer(company_list, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def loc_search2(request):
    location = Location.objects.order_by('location_name')
    serializer = LocationSerializer(location, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def companylevel_search(request, comp):
    levels = Level.objects.filter(company__in=
                                  Company.objects.filter(company_name__icontains=comp
                                                         )).distinct('level_name').order_by('level_name')
    serializer = LevelSerializer(levels, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def tag_search(request):
    tag = Tag.objects.distinct('tag_name').order_by(
        'tag_name')
    serializer = TagSerializer(tag, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def all_search(request):
    if 'application/json' not in request.content_type:
        return Response("Content type should be 'application/json'.", status=status.HTTP_400_BAD_REQUEST)
    try:
        company = request.data['company']
        location = request.data['location']
        level = request.data['level']
        tag = request.data['tag']
    except:
        return Response('Input JSON form invalid, go read README',
                        status=status.HTTP_400_BAD_REQUEST)
    employees = Employee.objects.none()
    if not location:
        location = Location.objects
    else:
        location = Location.objects.filter(location_name__icontains=location)

    if not company:
        if not level:
            if not tag:
                for l in location.iterator():
                    employees |= l.employee_set.select_related('level__company', 'tag',
                                                               'level', 'gender', 'race', 'academic_level')
            else:
                for l in location.iterator():
                    employees |= l.employee_set.filter(tag__tag_name__icontains=
                                                       tag).select_related('level__company', 'tag',
                                                                           'level', 'gender', 'race', 'academic_level')
        else:
            if not tag:
                for l in location.iterator():
                    employees |= l.employee_set.filter(level__level_name__icontains=
                                                       level).select_related('level__company', 'tag',
                                                                             'level', 'gender', 'race',
                                                                             'academic_level')
            else:
                for l in location.iterator():
                    employees |= l.employee_set.filter(level__level_name__icontains=
                                                       level).filter(tag__tag_name__icontains=tag).select_related(
                        'level__company', 'tag',
                        'level', 'gender', 'race', 'academic_level')

    else:
        if not level:
            if not tag:
                for l in location.iterator():
                    employees |= l.employee_set.filter(level__company__company_name__icontains=
                                                       company).select_related('level__company', 'tag',
                                                                               'level', 'gender', 'race',
                                                                               'academic_level')
            else:
                for l in location.iterator():
                    employees |= l.employee_set.filter(level__company__company_name__icontains=
                                                       company).filter(tag__tag_name__icontains=
                                                                       tag).select_related('level__company', 'tag',
                                                                                           'level', 'gender', 'race',
                                                                                           'academic_level')
        else:
            if not tag:
                for l in location.iterator():
                    employees |= l.employee_set.filter(level__company__company_name__icontains=
                                                       company).filter(level__level_name__icontains=
                                                                       level).select_related('level__company', 'tag',
                                                                                             'level', 'gender', 'race',
                                                                                             'academic_level')
            else:
                for l in location.iterator():
                    employees |= \
                        l.employee_set.filter(level__company__company_name__icontains=
                                              company).filter(level__level_name__icontains=
                                                              level).filter(tag__tag_name__icontains=
                                                                            tag).select_related('level__company', 'tag',
                                                                                                'level', 'gender',
                                                                                                'race',
                                                                                                'academic_level')

    employees = employees.order_by('-totalyearlycompensation')
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def companyloc_search(request, comp):
    company = Company.objects.filter(company_name__icontains=comp)
    location = Location.objects.none()
    for c in company:
        location |= c.location_set.all()
    location = location.order_by('location_name').distinct('location_name')
    serializer = LocationSerializer(location, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def companylevel_search(request, comp, loc):
    levels = Level.objects.filter(company__in=
                                  Company.objects.filter(company_name__icontains=
                                                         comp).filter(location__location_name__icontains=
                                                                      loc)).distinct('level_name').order_by(
        'level_name')
    serializer = LevelSerializer(levels, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def companytag_search(request, comp, loc, level):
    tag = Tag.objects.filter(company__in=
                             Company.objects.filter(company_name__icontains=
                                                    comp).filter(location__location_name__icontains=
                                                                 loc)).filter(employee__level__level_name=
                                                                              level).distinct('tag_name').order_by(
        'tag_name')
    serializer = TagSerializer(tag, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def companystats(request, comp):
    if not comp:
        return Response('Company cannot be null', status=status.HTTP_400_BAD_REQUEST)
    company = Company.objects.filter(company_name__icontains=comp)
    companyList = []
    for c in company.iterator():
        json = {}
        employee = Employee.objects.filter(level__company=c)
        json['company'] = model_to_dict(c)
        g_null = employee.filter(gender__gender=None).count()
        g_male = employee.filter(gender__gender='male').count()
        g_female = employee.filter(gender__gender='female').count()
        g_other = employee.filter(gender__gender='other').count()
        gender = {'null': g_null,
                  'male': g_male,
                  'female': g_female,
                  'other': g_other}
        json['gender'] = gender
        r_null = employee.filter(race__race=None).count()
        r_white = employee.filter(race__race='White').count()
        r_asian = employee.filter(race__race='Asian').count()
        r_hisp = employee.filter(race__race='Hispanic / Latino').count()
        r_two = employee.filter(race__race='Two or More Races').count()
        r_black = employee.filter(race__race='Black or African American').count()
        r_hawaii = employee.filter(race__race='Native Hawaiian or Other Pacific Islander').count()
        r_indian = employee.filter(race__race='American Indian or Alaska Native').count()
        race = {'null': r_null,
                'White': r_white,
                'Asian': r_asian,
                'Hispanic / Latino': r_hisp,
                'Two or More Races': r_two,
                'Black or African American': r_black,
                'Native Hawaiian or Other Pacific Islander': r_hawaii,
                'American Indian or Alaska Native': r_indian}
        json['race'] = race
        a_null = employee.filter(academic_level__acad_level=None).count()
        a_master = employee.filter(academic_level__acad_level='Master').count()
        a_bach = employee.filter(academic_level__acad_level='Bachelor').count()
        a_phd = employee.filter(academic_level__acad_level='Doctorate (PhD)').count()
        a_dropout = employee.filter(academic_level__acad_level='Some college coursework completed').count()
        a_highs = employee.filter(academic_level__acad_level='High school or equivalent').count()
        a_tech = employee.filter(academic_level__acad_level='Technical or occupational certificate').count()
        a_asso = employee.filter(academic_level__acad_level='Associate Degree').count()
        academic_level = {'null': a_null,
                          'Master': a_master,
                          'Bachelor': a_bach,
                          'Doctorate (PhD)': a_phd,
                          'Some college coursework completed': a_dropout,
                          'High school or equivalent': a_highs,
                          'Technical or occupational certificate': a_tech,
                          'Associate Degree': a_asso}
        json['academic_level'] = academic_level
        json['levels'] = c.level_set.all().values('level_name').distinct().order_by('level_name')
        json['totalyearlycompensation'] = employee.aggregate(Avg('totalyearlycompensation'))
        companyList.append(json)
    return Response(companyList)
