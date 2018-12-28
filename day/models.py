from django.db import models
from datetime import datetime

class Default_School_Day(models.Model):
	school=models.ForeignKey('school.School', on_delete=models.CASCADE)
	start_time=models.DateTimeField()
	slot_length=models.IntegerField()
	num_slots=models.IntegerField()
	
	class Meta:
		verbose_name="Default Day"
	
	def __str__(self):
		return '%s on %s' %(self.school.name, self.start_time.strftime("%B %d, %Y"))
			
class Alt_Klass_Day(models.Model):
	klass=models.ForeignKey('klass.Klass', on_delete=models.CASCADE, verbose_name="Class")
	start_time=models.DateTimeField()
	slot_length=models.IntegerField()
	num_slots=models.IntegerField()
	
	class Meta:
		verbose_name="Alternate Class Day"
	
	def __str__ (self):
		return '%s in %s on %s' %(self.klass.class_name, self.klass.school.name, self.start_time.strftime("%B %d, %Y"))
		
		