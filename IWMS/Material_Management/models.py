from django.db import models

# Create your models here.
class WeldingMaterial(models.Model):
	grade = models.CharField(max_length=50,blank=True,null=True)
	specifications = models.CharField(max_length=50,blank=True,null=True)
	price = models.FloatField(blank=True,null=True)
	def __str__(self):
		return self.grade 

class Auxiliary(models.Model):
	name = models.CharField(max_length=50,blank=True,null=True)
	description = models.TextField(blank=True,null=True)
	price = models.FloatField(blank=True,null=True)
	def __str__(self):
		return self.name

class ProtectiveGas(models.Model):
	name = models.CharField(max_length=50,blank=True,null=True)
	price = models.FloatField(blank=True,null=True)
	def __str__(self):
		return self.name

class WeldingMachine(models.Model):
	name = models.CharField(max_length=50,blank=True,null=True)
	specifications = models.CharField(max_length=50,blank=True,null=True)
	service_life = models.IntegerField(blank=True,null=True)
	storage_time = models.DateTimeField(blank=True,null=True)
	price = models.FloatField(blank=True,null=True)
	def __str__(self):
		return self.name

class BaseMetal(models.Model):
	specifications = models.CharField(max_length=50,blank=True,null=True)
	textrue = models.CharField(max_length=50,blank=True,null=True)
	price = models.FloatField(blank=True,null=True)
	def __str__(self):
		return self.specifications