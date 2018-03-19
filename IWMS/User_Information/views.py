# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def person_center(request):
    pass
    return render(request, 'User_Information/person_center.html')

@login_required
def setting(request):
    pass
    return render(request, 'User_Information/setting.html')

@login_required
def usercenter(request):
    pass
    return render(request, 'User_Information/usercenter.html')
