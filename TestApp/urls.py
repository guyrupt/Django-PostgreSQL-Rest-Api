from django.conf.urls import url
from django.urls.resolvers import URLPattern
from TestApp import views


urlpatterns = [
    url(r'^table1$', views.table1Api),
    url(r'^table1/([0-9]+)$',views.table1Api)
]