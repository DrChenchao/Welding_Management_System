# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

app_name = 'Staff_Management'
urlpatterns = [
    url(r'^staff_management/$',views.staff_management,name='staff_management'),
    url(r'^department_creat/$',views.department_creat,name='department_creat'),
    url(r'^department_edit/$',views.department_edit,name='department_edit'),
    url(r'^department_delete/$',views.department_delete,name='department_delete'),
]
