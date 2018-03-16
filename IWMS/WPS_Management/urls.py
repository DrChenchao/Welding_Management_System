# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

app_name = 'WPS_Management'
urlpatterns = [
    url(r'^wps_management/$',views.wps_management,name='wps_management')
]