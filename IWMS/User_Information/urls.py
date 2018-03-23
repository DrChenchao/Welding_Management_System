# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

app_name = 'User_Information'
urlpatterns = [
url(r'^edit_staff/$', views.edit_staff, name='edit_staff'),
	url(r'$', views.usercenter, name='usercenter'),
    
    url(r'^person_center/$', views.person_center, name='person_center'),
]