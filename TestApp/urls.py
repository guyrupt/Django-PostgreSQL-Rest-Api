from os import name
from django.urls import path
from TestApp import views

urlpatterns = [
    path('', views.apiOverview),
    path('data/', views.addInstance, name='add-data'),
    path('location/<str:loc>/', views.loc_search, name='search-location'),
    path('company/', views.companies, name='companies-list'),
    path('locations/', views.loc_search2, name='loc-search'),
    path('companylevels/<str:comp>', views.companylevel_search, name='comp-level-search'),
    path('tags/', views.tag_search, name='comp-tag-search'),
    path('search', views.all_search, name='4-search'),
    path('companystats/<str:comp>', views.companystats, name='company-stats'),
    path('companyloc/<str:comp>', views.companyloc_search, name='comp-loc-search'),
    path('companylevel/<str:comp>/<str:loc>', views.companylevel_search, name='comp-level-loc-search'),
    path('companytag/<str:comp>/<str:loc>/<str:level>', views.companytag_search, name='comp-tag-search')
]
