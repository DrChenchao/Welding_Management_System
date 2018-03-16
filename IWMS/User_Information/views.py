# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.


def person_center(request):
    pass
    return render(request, 'User_Information/person_center.html')


def setting(request):
    pass
    return render(request, 'User_Information/setting.html')


def usercenter(request):
    pass
    return render(request, 'User_Information/usercenter.html')