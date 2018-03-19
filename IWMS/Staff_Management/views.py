# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from Staff_Management.models import *
from django.http import HttpResponse
# Create your views here.

@login_required
def staff_management(request):
	departments = Department.objects.all()
	return render(request, 'Staff_Management/staff_management.html',locals())

@login_required
def department_creat(request):
	name = "";
	if request.method == 'GET':
		name = request.GET['name']
		p = Department(name = name)
		p.save()
	return HttpResponse(request.GET['name'])

@login_required
def department_edit(request):
	name = "";
	old_content="";
	if request.method == 'GET':
		name = request.GET['name']
		old_content = request.GET['old_content']
		p = Department.objects.filter(name=old_content).update(name = name)
	return HttpResponse(name)

@login_required
def department_delete(request):
	old_content="";
	if request.method == 'GET':
		old_content = request.GET['old_content']
		Department.objects.filter(name=old_content).delete();
	return HttpResponse(None)