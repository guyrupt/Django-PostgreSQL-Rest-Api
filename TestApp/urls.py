from django.urls import path
from TestApp import views


urlpatterns = [
    path('', views.apiOverview),
    path('tablelist/', views.tableList, name='tablelist'),
    path('tablelist/<str:pk>', views.tableItem, name= 'tableItem')
]