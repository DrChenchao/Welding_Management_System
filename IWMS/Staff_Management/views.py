# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from Staff_Management.models import *
from django.http import HttpResponse
from Staff_Management.forms import *
from django.http import QueryDict
from django.http import HttpResponseRedirect
# from django.forms.models import model_to_dict
from django.core import serializers
# Create your views here.

@login_required
def staff_management(request):
	departments = Department.objects.all()
	DepartmentPosts = DepartmentPost.objects.all()
	staffs = Staff.objects.all()
	context_dict = {'departments': departments, 'DepartmentPosts': DepartmentPosts, 'staffs': staffs}
	return render(request, 'Staff_Management/staff_management.html',context = context_dict)

@login_required
def welder_management(request):
	welders = Welder.objects.all()
	return render(request, 'Staff_Management/welder_management.html',locals())

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

@login_required
def staff_create(request):
	departmentposts = DepartmentPost.objects.all()
	result = serializers.serialize('json', departmentposts)
	return HttpResponse(result)

@login_required
def staff_edit(request):
	departmentposts = DepartmentPost.objects.all()
	result = serializers.serialize('json', departmentposts)
	return HttpResponse(result)

@login_required
def staff_create_confirm(request):
	if request.method == 'GET':
		username = request.GET['username']
		email = request.GET['email']
		phonenumber = request.GET['telephone']
		post = request.GET['post']
		password = '12345678'
		u = User(username = username, email=email)
		u.set_password(password)
		u.is_staff = True
		u.save();
		d = DepartmentPost.objects.get(id = post)
		p = Staff(user = u, telephone_number = phonenumber, post = d)
		p.save();
	return HttpResponse(None)

@login_required
def staff_edit_confirm(request):
	if request.method == 'GET':
		staff_ID = request.GET['staff_ID']
		username = request.GET['username']
		email = request.GET['email']
		phonenumber = request.GET['telephone']
		post = request.GET['post']
		u = User.objects.filter(id=staff_ID).update(username=username,email=email)
		d = DepartmentPost.objects.get(id = post)
		p = Staff.objects.filter(user = User.objects.get(id=staff_ID)).update(telephone_number = phonenumber, post = d)
	return HttpResponse(None)

@login_required
def staff_delete_confirm(request):
	if request.method == 'GET':
		staff_ID = request.GET['staff_ID']
		Staff.objects.filter(user = User.objects.get(id=staff_ID)).delete()
		User.objects.filter(id=staff_ID).delete()
	return HttpResponse(None)

@login_required
def welder_create(request):
	form = WelderForm()
	if request.method == 'POST':
		form = WelderForm(request.POST)
		if form.is_valid():
			welder = form.save(commit=True)
			return HttpResponseRedirect('/Staff_Management/welder_management')
		else:
			print(form.errors)
	return render(request, 'Staff_Management/welder_create.html', {'form': form})

@login_required
def welder_edit(request, staffid):
	if request.method == 'POST':
		form = WelderForm_edit(request.POST)
		if form.is_valid():
			temp= form.save(commit = False)
			Welder.objects.filter(staff=Staff.objects.get(id = staffid)).update(
				qualification=temp.qualification,expiry_date=temp.expiry_date,prolongation_date=temp.prolongation_date)
			return HttpResponseRedirect('/Staff_Management/welder_management')
		else:
			print(form.errors)
	else:
		staff_ID = request.GET['staff_ID']
		welder = Welder.objects.get(staff = Staff.objects.get(id = staff_ID))
		qdict = QueryDict('', mutable=True)
		qdict.update(welder.__dict__)
		form = WelderForm_edit(qdict)
	return render(request, 'Staff_Management/welder_edit.html', {'form': form, 'staffid': staff_ID})

@login_required
def welder_delete(request):
	if request.method == 'GET':
		staff_ID = request.GET['staff_ID']
		print(staff_ID)
		Welder.objects.filter(staff = Staff.objects.get(id=staff_ID)).delete()
	return HttpResponse(None)
