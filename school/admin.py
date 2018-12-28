from django.contrib import admin
from .models import School
from day.models import Default_School_Day

class Default_School_DayInline(admin.TabularInline):
	model=Default_School_Day
	min_num=1

class SchoolAdmin(admin.ModelAdmin):
	inlines = [
		Default_School_DayInline,
		]

admin.site.register(School, SchoolAdmin)
