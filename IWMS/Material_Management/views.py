# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def auxilary_material(request):
    pass
    return render(request, 'Material_Management/auxilary_material.html')

@login_required
def base_metal(request):
    pass
    return render(request, 'Material_Management/base_metal.html')

@login_required
def welding_gas(request):
    pass
    return render(request, 'Material_Management/welding_gas.html')

@login_required
def welding_material(request):
    pass
    return render(request, 'Material_Management/welding_material.html')

@login_required
def welding_torch(request):
    pass
    return render(request, 'Material_Management/welding_torch.html')

