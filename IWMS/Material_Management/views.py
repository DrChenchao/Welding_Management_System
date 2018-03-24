# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from Material_Management.models import *
from Material_Management.forms import *
from django.http import HttpResponseRedirect
from django.http import HttpResponse

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
def welding_machine(request):
    weldingmachines = WeldingMachine.objects.all()
    return render(request, 'Material_Management/welding_machine.html',locals())


@login_required
def creat_auxilary_material(request):
    form = AuxiliaryForm()
    if request.method == 'POST':
        form = AuxiliaryForm(request.POST,)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/Material_Management/auxilary_material/')
        else:
            print(form.errors)
    return render(request, 'Material_Management/create_auxilary_material.html', {'form': form})
@login_required
def edit_auxilary_material(request, ID):
    if request.method == 'POST':
        auxilary = Auxiliary.objects.get(id=ID)
        form = AuxiliaryForm(request.POST, instance=auxilary)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/Material_Management/auxilary_material')
        else:
            print(form.errors)
    else:
        auxilary_id = request.GET['ID']
        auxilary = Auxiliary.objects.get(id=auxilary_id)
        form = AuxiliaryForm(instance = auxilary)
    return render(request, 'Material_Management/edit_auxilary_material.html', {'form': form, 'ID': auxilary_id })
@login_required
def delete_auxilary_material(request):
    auxilary_id = request.GET['ID']
    auxilary = Auxiliary.objects.filter(id=auxilary_id).delete()
    return HttpResponse(None)


@login_required
def create_base_material(request):
    form = BaseMetalForm()
    if request.method == 'POST':
        form = BaseMetalForm(request.POST,)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/Material_Management/base_metal/')
        else:
            print(form.errors)
    return render(request, 'Material_Management/create_base_material.html', {'form': form})
@login_required
def edit_base_material(request, ID):
    if request.method == 'POST':
        base = BaseMetal.objects.get(id=ID)
        form = BaseMetalForm(request.POST, instance=base)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/Material_Management/base_metal')
        else:
            print(form.errors)
    else:
        base_id = request.GET['ID']
        base = BaseMetal.objects.get(id=base_id)
        form = BaseMetalForm(instance = base)
    return render(request, 'Material_Management/edit_base_material.html', {'form': form, 'ID': base_id })
@login_required
def delete_base_material(request):
    base_id = request.GET['ID']
    base = BaseMetal.objects.filter(id=base_id).delete()
    return HttpResponse(None)

@login_required
def create_welding_gas(request):
    form = ProtectiveGasForm()
    if request.method == 'POST':
        form = ProtectiveGasForm(request.POST,)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/Material_Management/welding_gas/')
        else:
            print(form.errors)
    return render(request, 'Material_Management/create_welding_gas.html', {'form': form})
@login_required
def edit_welding_gas(request, ID):
    if request.method == 'POST':
        base = ProtectiveGas.objects.get(id=ID)
        form = ProtectiveGasForm(request.POST, instance=base)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/Material_Management/welding_gas')
        else:
            print(form.errors)
    else:
        welding_gas_id = request.GET['ID']
        welding_gas = ProtectiveGas.objects.get(id=welding_gas_id)
        form = ProtectiveGasForm(instance = welding_gas)
    return render(request, 'Material_Management/edit_welding_gas.html', {'form': form, 'ID': welding_gas_id })
@login_required
def delete_welding_gas(request):
    welding_gas_id = request.GET['ID']
    welding_gas = ProtectiveGas.objects.filter(id=welding_gas_id).delete()
    return HttpResponse(None)

@login_required
def create_welding_material(request):
    form = WeldingMaterialForm()
    if request.method == 'POST':
        form = WeldingMaterialForm(request.POST,)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/Material_Management/welding_material/')
        else:
            print(form.errors)
    return render(request, 'Material_Management/create_welding_material.html', {'form': form})
@login_required
def edit_welding_material(request, ID):
    if request.method == 'POST':
        welding_material = WeldingMaterial.objects.get(id=ID)
        form = WeldingMaterialForm(request.POST, instance=welding_material)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/Material_Management/welding_material')
        else:
            print(form.errors)
    else:
        welding_material_id = request.GET['ID']
        welding_material = WeldingMaterial.objects.get(id=welding_material_id)
        form = WeldingMaterialForm(instance = welding_material)
    return render(request, 'Material_Management/edit_welding_material.html', {'form': form, 'ID': welding_material_id })
@login_required
def delete_welding_material(request):
    welding_material_id = request.GET['ID']
    welding_material = WeldingMaterial.objects.filter(id=welding_material_id).delete()
    return HttpResponse(None)

@login_required
def create_welding_machine(request):
    form = WeldingMachineForm()
    if request.method == 'POST':
        form = WeldingMachineForm(request.POST,)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/Material_Management/welding_machine/')
        else:
            print(form.errors)
    return render(request, 'Material_Management/create_welding_machine.html', {'form': form})
@login_required
def edit_welding_machine(request, ID):
    if request.method == 'POST':
        welding_machine = WeldingMachine.objects.get(id=ID)
        form = WeldingMachineForm(request.POST, instance=welding_machine)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/Material_Management/welding_machine')
        else:
            print(form.errors)
    else:
        welding_machine_id = request.GET['ID']
        welding_machine = WeldingMachine.objects.get(id=welding_machine_id)
        form = WeldingMachineForm(instance = welding_machine)
    return render(request, 'Material_Management/edit_welding_machine.html', {'form': form, 'ID': welding_machine_id })
@login_required
def delete_welding_machine(request):
    welding_machine_id = request.GET['ID']
    welding_machine = WeldingMachine.objects.filter(id=welding_machine_id).delete()
    return HttpResponse(None)


