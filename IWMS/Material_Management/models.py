from django.db import models

# Create your models here.
class WeldingMaterial(models.Model):
	grade = models.CharField(max_length=50,blank=True,null=True,help_text="请输入焊材牌号.",)
	specifications = models.CharField(max_length=50,blank=True,null=True,help_text="请输入焊材规格.",)
	price = models.FloatField(blank=True,null=True,help_text="请输入价格.",)
	def __str__(self):
		return self.grade 

class Auxiliary(models.Model):
	name = models.CharField(max_length=50,blank=True,null=True,help_text="请输入辅材名字.",)
	description = models.TextField(blank=True,null=True,help_text="辅材描述.",)
	price = models.FloatField(blank=True,null=True,help_text="请输入辅材价格.",)
	def __str__(self):
		return self.name

class ProtectiveGas(models.Model):
	name = models.CharField(max_length=50,blank=True,null=True,help_text="请输入保护气名字.",)
	price = models.FloatField(blank=True,null=True,help_text="请输入保护气价格.",)
	def __str__(self):
		return self.name

class WeldingMachine(models.Model):
	name = models.CharField(max_length=50,blank=True,null=True,help_text="请输入焊机名字.",)
	specifications = models.CharField(max_length=50,blank=True,null=True,help_text="请输入焊机规格.",)
	service_life = models.IntegerField(blank=True,null=True,help_text="请输入使用年限.",)
	storage_time = models.DateTimeField(blank=True,null=True,help_text="请输入入库时间.",)
	price = models.FloatField(blank=True,null=True,help_text="请输入焊机价格.",)
	def __str__(self):
		return self.name

class BaseMetal(models.Model):
	specifications = models.CharField(max_length=50,blank=True,null=True,help_text="请输入母材规格.",)
	textrue = models.CharField(max_length=50,blank=True,null=True,help_text="请输入母材材质.",)
	price = models.FloatField(blank=True,null=True,help_text="请输入母材价格.",)
	def __str__(self):
		return self.specifications