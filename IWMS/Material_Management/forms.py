from Material_Management.models import *
from django import forms

class WeldingMaterialForm(forms.ModelForm):
	class Meta:
		model = WeldingMaterial
		fields = ('grade','specifications','price',)

class AuxiliaryForm(forms.ModelForm):
	class Meta:
		model = Auxiliary
		fields = ('name','description','price',)

class ProtectiveGasForm(forms.ModelForm):
	class Meta:
		model = ProtectiveGas
		fields = ('name','price',)

class WeldingMachineForm(forms.ModelForm):
	class Meta:
		model = WeldingMachine
		fields = ('name','specifications','service_life',
			'storage_time','price',)

class BaseMetalForm(forms.ModelForm):
	class Meta:
		model = BaseMetal
		fields = ('specifications','textrue','price',)