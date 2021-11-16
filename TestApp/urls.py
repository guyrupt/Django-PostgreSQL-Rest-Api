from os import name
from django.urls import path
from TestApp import views

urlpatterns = [
    path('', views.apiOverview),
    path('data/', views.addInstance, name='add-data'),
    path('location/<str:loc>/', views.loc_search, name='search-location'),
    path('company/<str:comp>', views.company_search, name='search-company'),
    path('company/', views.companies, name='companies-list'),
    path('locations/', views.loc_search, name='loc-search'),
    path('companylevels/<str:comp>', views.companylevel_search, name='comp-level-search'),
    path('tags/', views.tag_search, name='comp-tag-search'),
    path('search', views.all_search, name='4-search')
]
