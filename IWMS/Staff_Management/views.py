# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from Staff_Management.models import *
from django.http import HttpResponse
from Staff_Management.forms import *
from django.http import QueryDict
from django.http import HttpResponseRedirect
# Create your views here.

@login_required
def staff_management(request):
	departments = Department.objects.all()
	DepartmentPosts = DepartmentPost.objects.all()
	context_dict = {'departments': departments, 'DepartmentPosts': DepartmentPosts}
	return render(request, 'Staff_Management/staff_management.html',context = context_dict)

@login_required
def department_creat(request):
	name = "";
	if request.method == 'GET':
		name = request.GET['name']
		p = Department(name = name)
		p.save()
	return HttpResponse(name)

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

@login_required
def add_post(request):
	form = PostForm()
	if request.method == 'POST':
		print(request.POST)
		form = PostForm(request.POST)
		if form.is_valid():
			form.save(commit=True)
			return HttpResponseRedirect('/Staff_Management/staff_management')
		else:
			print(form.errors)
	return render(request, 'Staff_Management/add_post.html', {'form': form})

@login_required
def edit_post(request, departmentpost_id):
	departmentpost = DepartmentPost.objects.get(id = departmentpost_id)
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			departmentpost.delete();
			form.save(commit=True)
			return HttpResponseRedirect('/Staff_Management/staff_management')
		else:
			print(form.errors)
	else:
		qdict = QueryDict('', mutable=True)
		qdict.update(departmentpost.__dict__)
		form = PostForm(qdict)
	return render(request, 'Staff_Management/edit_post.html', {'form': form, 'department_id': departmentpost_id})

@login_required
def delete_post(request, departmentpost_id):
	departmentpost = DepartmentPost.objects.get(id = departmentpost_id)
	departmentpost.delete();
	return HttpResponseRedirect('/Staff_Management/staff_management')
