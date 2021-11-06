from os import name
from django.urls import path
from TestApp import views


urlpatterns = [
    path('', views.apiOverview),
    path('data/', views.addInstance, name='add-data'),
    path('location/<str:loc>/', views.loc_search, name = 'search-location'),
    path('company/<str:comp>', views.company_search, name = 'search-company'),

]