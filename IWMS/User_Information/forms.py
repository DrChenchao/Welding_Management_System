from Staff_Management.models import *
from django import forms

class StaffForm(forms.ModelForm):
	class Meta:
		model = Staff
		fields = ('working_address','home_address','telephone_number',
			'id_number','nationality','gender','birth_date','Photo',)
	def __init__(self, *args, **kwargs):
		super(StaffForm, self).__init__(*args, **kwargs)
		for field_name in self.base_fields:
			field = self.base_fields[field_name]
			field.widget.attrs.update({"class":"form-control"})
