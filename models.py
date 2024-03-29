from django.db import models

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

class WeldingMaterial(models.Model):
	grade = models.CharField(max_length=50,blank=True,null=True)
	specifications = models.CharField(max_length=50,blank=True,null=True)
	price = models.FloatField(blank=True,null=True)

class WeldingMaterialTechnology(models.Model):
	baking_temperature = models.IntegerField(blank=True,null=True)
	preservationg_time = models.IntegerField(blank=True,null=True)
	size = models.CharField(max_length=50,blank=True,null=True)
	weldingmaterial = models.ForeignKey(WeldingMaterial, on_delete=models.CASCADE,blank=True,null=True)

class Auxiliary(models.Model):
	name = models.CharField(max_length=50,blank=True,null=True)
	description = models.TextField(blank=True,null=True)
	price = models.FloatField(blank=True,null=True)

class ProtectiveGas(models.Model):
	name = models.CharField(max_length=50,blank=True,null=True)
	price = models.FloatField(blank=True,null=True)

class WeldingMachine(models.Model):
	name = models.CharField(max_length=50,blank=True,null=True)
	specifications = models.CharField(max_length=50,blank=True,null=True)
	service_life = models.IntegerField(blank=True,null=True)
	storage_time = models.DateTimeField(blank=True,null=True)
	price = models.FloatField(blank=True,null=True)

class BaseMetal(models.Model):
	specifications = models.CharField(max_length=50,blank=True,null=True)
	textrue = models.CharField(max_length=50,blank=True,null=True)
	price = models.FloatField(blank=True,null=True)

class ABaseMetal(models.Model):
	basemetal = models.ForeignKey(BaseMetal, on_delete=models.CASCADE,blank=True,null=True)
	size = models.CharField(max_length=50,blank=True,null=True)
	groove_type = models.IntegerField(blank=True,null=True)
	groove_parameter1 = models.FloatField(blank=True,null=True)
	groove_parameter2 = models.FloatField(blank=True,null=True)
	groove_parameter3 = models.FloatField(blank=True,null=True)
	thickness_type = models.IntegerField(blank=True,null=True)
	groove_machine_method = models.CharField(max_length=100,blank=True,null=True)

class BBaseMetal(models.Model):
	basemetal = models.ForeignKey(BaseMetal, on_delete=models.CASCADE,blank=True,null=True)
	size = models.CharField(max_length=50,blank=True,null=True)
	groove_type = models.IntegerField(blank=True,null=True)
	groove_parameter1 = models.FloatField(blank=True,null=True)
	groove_parameter2 = models.FloatField(blank=True,null=True)
	groove_parameter3 = models.FloatField(blank=True,null=True)
	thickness_type = models.IntegerField(blank=True,null=True)
	groove_machine_method = models.CharField(max_length=100,blank=True,null=True)

class WPS(models.Model):
	qualification_category = (
        ('A', 'Senior Welding Technician'),
        ('B', 'Welding Technician'),
        ('C', 'Senior Welder'),
        ('D', 'Intermediate Welder'),
        ('E', 'Primary Welder'),
    )
	defect_detecting = models.CharField(max_length=100,blank=True,null=True)
	groove_clean_method = models.CharField(max_length=100,blank=True,null=True)
	weld_root_clean_method = models.CharField(max_length=100,blank=True,null=True)
	preheat_temperature = models.IntegerField(blank=True,null=True)
	preheat_preservation_method = models.IntegerField(blank=True,null=True)
	interlayer_temperature = models.IntegerField(blank=True,null=True)
	PWHT = models.CharField(max_length=100,blank=True,null=True)
	welder_qualification_demand = models.CharField(max_length=1, choices=qualification_category,blank=True,null=True)
	mark = models.TextField(blank=True,null=True)

class MechanicalPropertiesOfWelds(models.Model):
	category = (
        ('O', 'ordinary'),
        ('S', 'strong'),
        ('E', 'extremely strong'),
    )
	mpwid = models.OneToOneField(WPS,on_delete=models.CASCADE,primary_key=True,)
	tensile_properties = models.CharField(max_length=1, choices=category,blank=True,null=True)
	bending_strength = models.CharField(max_length=1, choices=category,blank=True,null=True)
	impact_toughness = models.CharField(max_length=1, choices=category,blank=True,null=True)
	fatigue_strength = models.CharField(max_length=1, choices=category,blank=True,null=True)
	heat_resistant_crack = models.CharField(max_length=1, choices=category,blank=True,null=True)
	corrosion_resistance = models.CharField(max_length=1, choices=category,blank=True,null=True)
	hardness = models.CharField(max_length=1, choices=category,blank=True,null=True)
	anti_lamellar_tearing = models.CharField(max_length=1, choices=category,blank=True,null=True)

class WeldConditionParameter(models.Model):
	current_polarity_category = (('N', 'DCEN'),('P', 'DCEP'),)
	wps = models.ForeignKey(WPS,on_delete=models.CASCADE,blank=True,null=True)
	welding_sequence = models.IntegerField(blank=True,null=True)
	layer = models.IntegerField(blank=True,null=True)
	path = models.IntegerField(blank=True,null=True)
	welding_method = models.CharField(max_length=50,blank=True,null=True)
	welding_material = models.ForeignKey(WeldingMaterial,on_delete=models.CASCADE,blank=True,null=True)
	auxiliary = models.ForeignKey(Auxiliary,on_delete=models.CASCADE,blank=True,null=True)
	current_polarity = models.CharField(max_length=1, choices=current_polarity_category,blank=True,null=True)
	max_current = models.FloatField(blank=True,null=True)
	min_current = models.FloatField(blank=True,null=True)
	max_voltage = models.FloatField(blank=True,null=True)
	min_voltage = models.FloatField(blank=True,null=True)
	welding_speed = models.FloatField(blank=True,null=True)
	protective_gas = models.ForeignKey(ProtectiveGas,on_delete=models.CASCADE,blank=True,null=True)
	tungsten_pole_diameter = models.FloatField(blank=True,null=True)
	nozzle_diameter = models.FloatField(blank=True,null=True)
	frontal_gas_flow = models.FloatField(blank=True,null=True)
	back_gas_flow = models.FloatField(blank=True,null=True)
	welding_machine = models.ForeignKey(WeldingMachine,on_delete=models.CASCADE,blank=True,null=True)

class WeldArtwork(models.Model):
	joint_type_category = (
        ('b', 'butt joint'),
        ('f', 'fillet joint'),
    )
	layer_pass_type_category = (
        ('A', '1-1'),
        ('B', '1-1,2-1'),
        ('C', '1-1,2-2'),
        ('D', '1-1,2-1,3-2'),
        ('E', '1-1,2-2,3-3'),
        ('F', '1-1,2-2,3-3,4-4'),
        ('G', '1-1,2-2,3-3,4-4,5-5'),
        ('H', '1-1,2-1,3-1'),
        ('I', '1-1,2-1,3-1,4-1'),
        ('J', '1-1,2-1,3-2,4-2'),
        ('K', 'None'),
    )
	relative_position_category = (
        ('A', 'Top'),
        ('B', 'Middle'),
        ('C', 'bottom'),
    )
	waid = models.OneToOneField(WPS,on_delete=models.CASCADE,primary_key=True)
	joint_type = models.CharField(max_length=1, choices=joint_type_category,blank=True,null=True)
	gap = models.IntegerField(blank=True,null=True)
	relative_position = models.CharField(max_length=1, choices=relative_position_category,blank=True,null=True)
	top_layer_pass_type= models.CharField(max_length=1, choices=layer_pass_type_category,blank=True,null=True)
	bottom_layer_pass_type= models.CharField(max_length=1, choices=layer_pass_type_category,blank=True,null=True)
	A_base_metal = models.ForeignKey(ABaseMetal,on_delete=models.CASCADE,blank=True,null=True)
	B_base_metal = models.ForeignKey(BBaseMetal,on_delete=models.CASCADE,blank=True,null=True)

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

