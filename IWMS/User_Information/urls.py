# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

app_name = 'User_Information'
urlpatterns = [
    url(r'^person_center/$', views.person_center,name='person_center'),
    url(r'^setting/$', views.setting,name='setting'),
    url(r'', views.usercenter,name='usercenter'),
]