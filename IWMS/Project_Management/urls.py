# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

app_name = 'Project_Management'
urlpatterns = [
    url(r'^project_management/$', views.project_management,name='project_management'),
]
