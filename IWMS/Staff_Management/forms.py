from django import forms
from Staff_Management.models import *

class PostForm(forms.ModelForm):
	department_id = forms.ModelChoiceField(queryset = Department.objects.all(), help_text="请输入部门名称.",)
	department_post_name = forms.CharField(max_length=30, help_text="请输入岗位名称.")
	access_right_1 = forms.BooleanField(help_text="员工管理.", required=False)
	access_right_2 = forms.BooleanField(help_text="焊材管理.", required=False)
	access_right_3 = forms.BooleanField(help_text="WPS管理.", required=False)
	access_right_4 = forms.BooleanField(help_text="焊接项目管理.", required=False)
	class Meta:
		# Provide an association between the ModelForm and a model
		model = DepartmentPost
		fields = ('department_id','department_post_name','access_right_1','access_right_2','access_right_3','access_right_4',)
