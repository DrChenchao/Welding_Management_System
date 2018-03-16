# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.


def auxilary_material(request):
    pass
    return render(request, 'Material_Management/auxilary_material.html')


def base_metal(request):
    pass
    return render(request, 'Material_Management/base_metal.html')


def welding_gas(request):
    pass
    return render(request, 'Material_Management/welding_gas.html')


def welding_material(request):
    pass
    return render(request, 'Material_Management/welding_material.html')


def welding_torch(request):
    pass
    return render(request, 'Material_Management/welding_torch.html')

