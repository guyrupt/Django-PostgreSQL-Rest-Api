from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from TestApp.models import table1 
from TestApp.serializers import table1Serializer 
# Create your views here.

@csrf_exempt
def table1Api(request, id=0):
    if request.method == 'GET':
        table11 = table1.objects.all()
        table11_serializer = table1Serializer(table11, many=True)
        return JsonResponse(table11_serializer.data, safe=False)
    elif request.method == 'POST':
        table11_data = JSONParser().parse(request)
        table11_serializer = table1Serializer(data=table11_data)
        if table11_serializer.is_valid():
            table11_serializer.save()
            return JsonResponse("Add Success", safe=False)
        return JsonResponse("Add Fail", safe=False)
    elif request.method == 'PUT':
        table11_data = JSONParser().parse(request)
        table11 = table1.objects.get(tb1Id=table11_data['tb1Id'])
        table11_serializer = table1Serializer(table11,data=table11_data)
        if table11_serializer.is_valid():
            table11_serializer.save()
            return JsonResponse("Update Success", safe=False)
        return JsonResponse("Update Fail", safe=False)
    elif request.method == 'DELETE':
        table11 = table1.objects.get(tb1Id=id)
        table11.delete()
        return JsonResponse("Delete Success", safe=False)