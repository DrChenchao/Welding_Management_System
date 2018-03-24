# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from Staff_Management.models import *
from User_Information.forms import *
from django.http import HttpResponseRedirect
import os
from django.core.files.base import ContentFile
from IWMS.settings import MEDIA_DIR
# Create your views here.
@login_required
def person_center(request):
    pass
    return render(request, 'User_Information/person_center.html')

@login_required
def edit_staff(request):
	staff = Staff.objects.get_or_create(user = User.objects.get(id=request.user.id))[0]
	imagename=str(staff.Photo)
	form = StaffForm(instance = staff)
	#print("test")
	if request.method == 'POST':
		form = StaffForm(request.POST, request.FILES, instance = staff)
		if form.is_valid():
			if 'Photo' in request.FILES:
				if imagename == None:
					imagefile = os.path.join(MEDIA_DIR, imagename)
					# print(imagefile)
					os.remove(imagefile)
			form.save(commit=True)
			return HttpResponseRedirect('User_Information/')
		else:
			form = StaffForm(instance = staff)
	return render(request, 'User_Information/editstaff.html', {'form': form})

@login_required
def usercenter(request):
	staff = Staff.objects.get(user = User.objects.get(id=request.user.id))
	q = Welder.objects.filter(staff = staff)
	if q.exists():
		return render(request, 'User_Information/usercenter.html',{'staff': staff, 'welder': q[0]})
	else:
		return render(request, 'User_Information/usercenter.html',{'staff': staff})
