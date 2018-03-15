from django.db import models

# Create your models here.
class Department(models.Model):
	name = models.CharField(max_length=20)

class DepartmentPost(models.Model):
	department_id = models.ForeignKey(Department,on_delete=models.CASCADE,)
	department_post_name = models.CharField(max_length=30)

class Staff(models.Model):
	gender_category = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
	name = models.CharField(max_length=20)
	post = models.ForeignKey(DepartmentPost,on_delete=models.CASCADE,)
	working_address = models.CharField(max_length=100)
	home_address = models.CharField(max_length=100,blank=True,null=True)
	emile = models.EmailField(max_length=254)
	telephone_number = models.CharField(max_length=20)
	id_number = models.CharField(max_length=20)
	nationality = models.CharField(max_length=10)
	gender = models.CharField(max_length=1, choices=gender_category)
	birth_date = models.DateTimeField()
	Photo = models.ImageField(upload_to='Staff/',blank=True)
	performance = models.DecimalField(max_digits=5, decimal_places=2,blank=True,null=True)

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