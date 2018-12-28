from django.db import models

class Slot(models.Model):
	klass=models.ForeignKey('klass.Klass', on_delete=models.CASCADE)
	start_time=models.DateTimeField()
	end_time=models.DateTimeField()
	not_available=models.BooleanField(default=False)
	
	def __str__(self):
		return '%s on %s at %s until %s' %(self.klass.class_name, self.start_time.strftime("%B %d"), self.start_time, self.end_time)
		