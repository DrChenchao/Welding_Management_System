# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

app_name = 'Material_Management'
urlpatterns = [
    url(r'^auxilary_material/$', views.auxilary_material,name='auxilary_material'),
    url(r'^base_metal/$', views.base_metal,name='base_metal'),
    url(r'^welding_gas/$', views.welding_gas,name='welding_gas'),
    url(r'^welding_material/$', views.welding_material,name='welding_material'),
    url(r'^welding_machine/$', views.welding_machine,name='welding_machine'),
    url(r'^creat_auxilary_material/$', views.creat_auxilary_material,name='creat_auxilary_material'),
    url(r'^edit_auxilary_material/(?P<ID>[\w\-]+)/$', views.edit_auxilary_material, name='edit_auxilary_material'),
    url(r'^delete_auxilary_material/$', views.delete_auxilary_material, name='delete_auxilary_material'),
    url(r'^create_base_material/$', views.create_base_material,name='create_base_material'),
    url(r'^edit_base_material/(?P<ID>[\w\-]+)/$', views.edit_base_material, name='edit_base_material'),
    url(r'^delete_base_material/$', views.delete_base_material, name='delete_base_material'),
    url(r'^create_welding_gas/$', views.create_welding_gas,name='create_welding_gas'),
    url(r'^edit_welding_gas/(?P<ID>[\w\-]+)/$', views.edit_welding_gas, name='edit_welding_gas'),
    url(r'^delete_welding_gas/$', views.delete_welding_gas, name='delete_welding_gas'),
    url(r'^create_welding_material/$', views.create_welding_material,name='create_welding_material'),
    url(r'^edit_welding_material/(?P<ID>[\w\-]+)/$', views.edit_welding_material, name='edit_welding_material'),
    url(r'^delete_welding_material/$', views.delete_welding_material, name='delete_welding_material'),
    url(r'^create_welding_machine/$', views.create_welding_machine,name='create_welding_machine'),
    url(r'^edit_welding_machine/(?P<ID>[\w\-]+)/$', views.edit_welding_machine, name='edit_welding_machine'),
    url(r'^delete_welding_machine/$', views.delete_welding_machine, name='delete_welding_machine'),
]

