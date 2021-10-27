from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse

from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response

from TestApp.models import table1 
from TestApp.serializers import table1Serializer 
# Create your views here.

# @csrf_exempt
# def table1Api(request, id=0):
#     if request.method == 'GET':
#         table11 = table1.objects.all()
#         table11_serializer = table1Serializer(table11, many=True)
#         return JsonResponse(table11_serializer.data, safe=False)
#     elif request.method == 'POST':
#         table11_data = JSONParser().parse(request)
#         table11_serializer = table1Serializer(data=table11_data)
#         if table11_serializer.is_valid():
#             table11_serializer.save()
#             return JsonResponse("Add Success", safe=False)
#         return JsonResponse("Add Fail", safe=False)
#     elif request.method == 'PUT':
#         table11_data = JSONParser().parse(request)
#         table11 = table1.objects.get(tb1Id=table11_data['tb1Id'])
#         table11_serializer = table1Serializer(table11,data=table11_data)
#         if table11_serializer.is_valid():
#             table11_serializer.save()
#             return JsonResponse("Update Success", safe=False)
#         return JsonResponse("Update Fail", safe=False)
#     elif request.method == 'DELETE':
#         table11 = table1.objects.get(tb1Id=id)
#         table11.delete()
#         return JsonResponse("Delete Success", safe=False)

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List':'/tablelist/',
        'Item': '/tablelist/<str:pk>',
    }
    return Response(api_urls)

@api_view(['GET'])
def tableList(request):
    table_data = table1.objects.all()
    print(table_data)
    table_serializer = table1Serializer(table_data, many=True)
    return Response(table_serializer.data)

@api_view(['GET'])
def tableItem(request, pk):
    table_data = table1.objects.get(tb1Id=pk)
    table_serializer = table1Serializer(table_data, many=False)
    return Response(table_serializer.data)