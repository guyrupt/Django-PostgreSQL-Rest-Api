from os import name
from django.urls import path
from TestApp import views


urlpatterns = [
    path('', views.apiOverview),
    path('data/', views.addInstance, name='add-data')
]