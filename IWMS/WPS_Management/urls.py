# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

app_name = 'WPS_Management'
urlpatterns = [
    url(r'^wps_management/$',views.wps_management,name='wps_management'),
    url(r'^wps_management/(?P<wps_id>[0-9]+)/detail/$', views.wps_detail, name='wps_detail'),
    url(r'^wps_management/(?P<wps_id>[0-9]+)/edit/$', views.wps_edit, name='wps_edit'),
    url(r'^wps_management/(?P<wps_id>[0-9]+)/delete/$', views.wps_delete, name='wps_delete'),
]