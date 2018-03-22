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

class WelderForm(forms.ModelForm):
	qualification_category = (
        ('A', 'Senior Welding Technician'),
        ('B', 'Welding Technician'),
        ('C', 'Senior Welder'),
        ('D', 'Intermediate Welder'),
        ('E', 'Primary Welder'),
    )
	staff = forms.ModelChoiceField(queryset= Staff.objects.all(), help_text="用户:",)
	qualification  = forms.CharField(
		max_length=1,
        widget=forms.Select(choices=qualification_category), help_text="焊工资历:",
		)
	expiry_date = forms.DateField(required=False, help_text="到期时间:",)
	prolongation_date = forms.DateField(required=False, help_text="延期时间:",)
	class Meta:
		# Provide an association between the ModelForm and a model
		model = Welder
		fields = ('staff','qualification','expiry_date','prolongation_date',)

class WelderForm_edit(forms.ModelForm):
	qualification_category = (
        ('A', 'Senior Welding Technician'),
        ('B', 'Welding Technician'),
        ('C', 'Senior Welder'),
        ('D', 'Intermediate Welder'),
        ('E', 'Primary Welder'),
    )
	staff = forms.CharField(widget=forms.HiddenInput(), required=False)
	qualification  = forms.CharField(
		max_length=1,
        widget=forms.Select(choices=qualification_category), help_text="焊工资历:",
		)
	expiry_date = forms.DateField(required=False, help_text="到期时间:",)
	prolongation_date = forms.DateField(required=False, help_text="延期时间:",)
	class Meta:
		# Provide an association between the ModelForm and a model
		model = Welder
		fields = ('qualification','expiry_date','prolongation_date',)