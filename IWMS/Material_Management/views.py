# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from Material_Management.models import *
# Create your views here.

@login_required
def auxilary_material(request):
    auxilarys = Auxiliary.objects.all()
    return render(request, 'Material_Management/auxilary_material.html',locals())

@login_required
def base_metal(request):
    baseMetals = BaseMetal.objects.all()
    return render(request, 'Material_Management/base_metal.html',locals())

@login_required
def welding_gas(request):
    weldingGases = ProtectiveGas.objects.all()
    return render(request, 'Material_Management/welding_gas.html',locals())

@login_required
def welding_material(request):
    weldingMaterials = WeldingMaterial.objects.all()
    return render(request, 'Material_Management/welding_material.html',locals())

@login_required
def welding_torch(request):
    weldingTorchs = WeldingMachine.objects.all()
    return render(request, 'Material_Management/welding_torch.html',locals())

