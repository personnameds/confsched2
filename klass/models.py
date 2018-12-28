from django.db import models
from django.contrib.auth.models import User

##Currently 1 teacher per class
class Klass(models.Model):
	school=models.ForeignKey('school.School', on_delete=models.CASCADE)
	teacher=models.ForeignKey('Teacher', on_delete=models.PROTECT)
	room_num=models.CharField(max_length=5)
	class_name=models.CharField(max_length=10)
	
	class Meta:
		verbose_name="Class"
		verbose_name_plural="Classes"
	
	def __str__(self):
		return '%s %s %s' %(self.school.name, self.teacher.teacher_name, self.class_name)
			
class Teacher(models.Model):
	#user=models.OneToOneField(User, on_delete=models.CASCADE)
	teacher_name=models.CharField(max_length=50)

	def __str__(self):
		return self.teacher_name
			