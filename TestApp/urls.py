from django.urls import path
from TestApp import views


urlpatterns = [
    path('', views.table1Api),
]