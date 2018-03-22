# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

app_name = 'Staff_Management'
urlpatterns = [
    url(r'^staff_management/$',views.staff_management,name='staff_management'),
    url(r'^welder_management/$',views.welder_management,name='welder_management'),
    url(r'^department_creat/$',views.department_creat,name='department_creat'),
    url(r'^department_edit/$',views.department_edit,name='department_edit'),
    url(r'^department_delete/$',views.department_delete,name='department_delete'),
    url(r'^add_post/$', views.add_post, name='add_post'),
    url(r'^edit_post/(?P<departmentpost_id>[\w\-]+)/$', views.edit_post, name='edit_post'),
    url(r'^delete_post/(?P<departmentpost_id>[\w\-]+)/$', views.delete_post, name='delete_post'),
    url(r'^staff_create/$', views.staff_create, name='staff_create'),
    url(r'^staff_edit/$', views.staff_edit, name='staff_edit'),
    url(r'^staff_create_confirm/$', views.staff_create_confirm, name='staff_create_confirm'),
    url(r'^staff_edit_confirm/$', views.staff_edit_confirm, name='staff_edit_confirm'),
    url(r'^staff_delete_confirm/$', views.staff_delete_confirm, name='staff_delete_confirm'),
    url(r'^welder_create/$', views.welder_create, name='welder_create'),
    url(r'^welder_edit/(?P<staffid>[\w\-]+)/$', views.welder_edit, name='welder_edit'),
    url(r'^welder_delete/$', views.welder_delete, name='welder_delete'),

]
