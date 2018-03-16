# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

app_name = 'Material_Management'
urlpatterns = [
    url(r'^auxilary_material/$', views.auxilary_material,name='auxilary_material'),
    url(r'^base_metal/$', views.base_metal,name='base_metal'),
    url(r'^welding_gas/$', views.welding_gas,name='welding_gas'),
    url(r'^welding_material/$', views.welding_material,name='welding_material'),
    url(r'^welding_torch/$', views.welding_torch,name='welding_torch'),
]