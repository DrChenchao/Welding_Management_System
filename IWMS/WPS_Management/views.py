# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def wps_management(request):
    pass
    return render(request, 'WPS_Management/wps_management.html')