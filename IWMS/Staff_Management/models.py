from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
# Create your models here.
class Department(models.Model):
	name = models.CharField(max_length=20,unique=True)
	def __str__(self):
		return self.name

class DepartmentPost(models.Model):
	department_id = models.ForeignKey(Department,on_delete=models.CASCADE,)
	department_post_name = models.CharField(max_length=30,unique=True)
	access_right_1 = models.BooleanField(blank=True,default=False)
	access_right_2 = models.BooleanField(blank=True,default=False)
	access_right_3 = models.BooleanField(blank=True,default=False)
	access_right_4 = models.BooleanField(blank=True,default=False)
	def __str__(self):
		return self.department_post_name

class Staff(models.Model):
	gender_category = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
	user = models.OneToOneField(User,blank=True,null=True,on_delete=models.CASCADE,)
	post = models.ForeignKey(DepartmentPost,blank=True,null=True,on_delete=models.CASCADE,)
	working_address = models.CharField(max_length=100,blank=True,null=True)
	home_address = models.CharField(max_length=100,blank=True,null=True)
	telephone_number = models.CharField(max_length=20,blank=True,null=True,)
	id_number = models.CharField(max_length=20,blank=True,null=True,)
	nationality = models.CharField(max_length=10,blank=True,null=True,)
	gender = models.CharField(max_length=1, choices=gender_category,blank=True,null=True,)
	birth_date = models.DateTimeField(blank=True,null=True,)
	Photo = models.ImageField(upload_to='Staff/',blank=True,null=True,)
	performance = models.DecimalField(max_digits=5, decimal_places=2,blank=True,null=True)
	def __str__(self):
		return self.user.username

class Welder(models.Model):
	qualification_category = (
        ('A', 'Senior Welding Technician'),
        ('B', 'Welding Technician'),
        ('C', 'Senior Welder'),
        ('D', 'Intermediate Welder'),
        ('E', 'Primary Welder'),
    )
	staff = models.OneToOneField(Staff,on_delete=models.CASCADE,primary_key=True,)
	qualification  = models.CharField(max_length=1, choices=qualification_category,blank=True,null=True)
	expiry_date = models.DateTimeField(blank=True,null=True)
	prolongation_date = models.DateTimeField(blank=True,null=True)
	def __str__(self):
		return self.staff.user.username