from django.contrib import admin
from .models import Klass
from .models import Teacher
from day.models import Alt_Klass_Day, Default_School_Day
from schedule.models import Slot
from datetime import timedelta

class Alt_Klass_DayInline(admin.TabularInline):
	model=Alt_Klass_Day

class KlassAdmin(admin.ModelAdmin):
	inlines = [
		Alt_Klass_DayInline,
		]
	
	def save_formset(self, request, form, formset, change):
		klass=form.save()
		Slot.objects.filter(klass=klass).delete()
		
		instances=formset.save()
		
		if instances == []:
			instances=Default_School_Day.objects.all()

		for instance in instances:
			start_time=instance.start_time
			slot_length=instance.slot_length
		
			for i in range(instance.num_slots):
				end_time=start_time + timedelta(minutes=slot_length)
				slot=Slot(klass=klass,
					start_time=start_time,
					end_time=end_time,
					)
				slot.save()
				start_time=end_time

				


admin.site.register(Klass, KlassAdmin)
admin.site.register(Teacher)
