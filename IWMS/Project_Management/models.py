from django.db import models
from WPS_Management.models import *
from Staff_Management.models import *
# Create your models here.
class WeldingProject(models.Model):
	workshop_sketch = models.ImageField(upload_to='WeldingProject/')
	description = models.TextField(blank=True,null=True)

class TaskArrangementLocation(models.Model):
	x_coordinates = models.FloatField(blank=True,null=True)
	y_coordinates = models.FloatField(blank=True,null=True)
	description = models.TextField(blank=True,null=True)
	weldingproject = models.ForeignKey(WeldingProject,on_delete=models.CASCADE,blank=True,null=True)

class WeldingTask(models.Model):
	taskarrangementlocation = models.ForeignKey(TaskArrangementLocation,on_delete=models.CASCADE,blank=True,null=True)
	welder = models.ForeignKey(Welder,on_delete=models.CASCADE,blank=True,null=True)
	wps = models.ForeignKey(WPS,on_delete=models.CASCADE,blank=True,null=True)
	expected_welding_time = models.DateTimeField(blank=True,null=True)
	start_time_of_actual_welding = models.DateTimeField(blank=True,null=True)
	duration_time = models.IntegerField(blank=True,null=True)
	wps_deviation = models.CharField(max_length=100,blank=True,null=True)
	corrective_measures = models.TextField(blank=True,null=True)
	detection_result_of_tensile_properties = models.FloatField(blank=True,null=True)
	detection_result_of_fatigue_strength = models.FloatField(blank=True,null=True)
	detection_result_of_bending_strength = models.FloatField(blank=True,null=True)
	detection_result_of_frontal_melted_width = models.FloatField(blank=True,null=True)
	detection_result_of_back_melted_width = models.FloatField(blank=True,null=True)
	detection_result_of_penetration_depths = models.CharField(max_length=10)

class ActualWeldingData(models.Model):
	welding_task = models.ForeignKey(WeldingTask,on_delete=models.CASCADE,blank=True,null=True)
	time = models.TimeField(blank=True,null=True)
	current = models.FloatField(blank=True,null=True)
	voltage = models.FloatField(blank=True,null=True)
	sound = models.FloatField(blank=True,null=True)
	picture = models.ImageField(upload_to='ActualWeldingData/')
	prediction_of_tensile_properties = models.FloatField(blank=True,null=True)
	prediction_of_fatigue_strength = models.FloatField(blank=True,null=True)
	prediction_of_bending_strength = models.FloatField(blank=True,null=True)
	pore = models.NullBooleanField(blank=True)
	slag = models.NullBooleanField(blank=True)
	prediction_of_frontal_melt_width = models.FloatField(blank=True,null=True)
	prediction_of_back_melt_width = models.FloatField(blank=True,null=True)