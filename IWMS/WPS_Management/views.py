# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from WPS_Management.models import *
# Create your views here.

@login_required
def wps_management(request):
    wps = WPS.objects.all()
    context = []
    for i in wps:
        welding_method = ''
        for j in i.weldconditionparameter_set.all():
            welding_method = welding_method + j.welding_method + ','
        w = [{
            'id':i.id,
            'defect_detecting':i.defect_detecting,
            'welder_qualification_demand':i.welder_qualification_demand,
            'mark':i.mark,
            'welding_method': welding_method,
        }]

        context=context+w
    return render(request, 'WPS_Management/wps_management.html',context={'wps':context})


@login_required
def wps_detail(request, wps_id):
    wps = WPS.objects.get(id=wps_id)
    weldart = wps.weldartwork
    weldconditions = wps.weldconditionparameter_set.all()
    print(weldconditions[0])
    weldmachine0 = weldconditions[0].welding_machine
    weldgas0 = weldconditions[0].protective_gas
    weldauxiliary0 = weldconditions[0].auxiliary
    weldmaterialtech0 = weldconditions[0].welding_material
    try:
        weldmachine1 = weldconditions[1].welding_machine
        weldgas1 = weldconditions[1].protective_gas
        weldauxiliary1 = weldconditions[1].auxiliary
        weldmaterialtech1 = weldconditions[1].welding_material
    except IndexError:
        print('Index Error,Don\'t Have Another WeldingConditions')
    try:
        weldmachine2 = weldconditions[2].welding_machine
        weldgas2 = weldconditions[2].protective_gas
        weldauxiliary2 = weldconditions[2].auxiliary
        weldmaterialtech2 = weldconditions[2].welding_material
    except IndexError:
        print('Index Error,Don\'t Have Another WeldingConditions')
    return render(request, 'WPS_Management/wps_detail.html',locals())


@login_required
def wps_edit(request,wps_id):
    wps = WPS.objects.get(id=wps_id)
    weldart = wps.weldartwork
    weldconditions = wps.weldconditionparameter_set.all()
    print(weldconditions[0])
    weldmachine0 = weldconditions[0].welding_machine
    weldgas0 = weldconditions[0].protective_gas
    weldauxiliary0 = weldconditions[0].auxiliary
    weldmaterialtech0 = weldconditions[0].welding_material
    try:
        weldmachine1 = weldconditions[1].welding_machine
        weldgas1 = weldconditions[1].protective_gas
        weldauxiliary1 = weldconditions[1].auxiliary
        weldmaterialtech1 = weldconditions[1].welding_material
    except IndexError:
        print('Index Error,Don\'t Have Another WeldingConditions')
    try:
        weldmachine2 = weldconditions[2].welding_machine
        weldgas2 = weldconditions[2].protective_gas
        weldauxiliary2 = weldconditions[2].auxiliary
        weldmaterialtech2 = weldconditions[2].welding_material
    except IndexError:
        print('Index Error,Don\'t Have Another WeldingConditions')
    return render(request, 'WPS_Management/wps_edit.html',locals())


@login_required
def wps_delete(request,wps_id):
    wps = WPS.objects.get(id=wps_id)
    wps.delete()
    return HttpResponseRedirect('/WPS_Management/wps_management')
