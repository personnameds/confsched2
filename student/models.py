from django.db import models

class Student(models.Model):
	first_name=models.CharField(max_length=25)
	last_name=models.CharField(max_length=50)
	klass=models.ForeignKey('klass.Klass', on_delete=models.CASCADE)
	phone_number=models.CharField(max_length=15)
	email=models.EmailField(max_length=250)
	comment=models.TextField()
	slot=models.ForeignKey('schedule.Slot', on_delete=models.CASCADE)

	def __str__(self):
		return '%s %s in %s' %(self.first_name, self.last_name, self.klass.class_name)
		