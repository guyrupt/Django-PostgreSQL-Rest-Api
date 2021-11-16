from os import name
from django.urls import path
from TestApp import views

urlpatterns = [
    path('', views.apiOverview),
    path('data/', views.addInstance, name='add-data'),
    path('location/<str:loc>/', views.loc_search, name='search-location'),
    path('company/<str:comp>', views.company_search, name='search-company'),
    path('company/', views.companies, name='companies-list'),
    path('companyloc/<str:comp>', views.companyloc_search, name='comp-loc-search'),
    path('companylevel/<str:comp>/<str:loc>', views.companylevel_search, name='comp-level-search'),
    path('companytag/<str:comp>/<str:loc>/<str:level>', views.companytag_search, name='comp-tag-search')
]
