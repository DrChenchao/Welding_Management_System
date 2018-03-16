# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

app_name = 'Staff_Management'
urlpatterns = [
    url(r'^staff_management/$',views.staff_management,name='staff_management'),
]
