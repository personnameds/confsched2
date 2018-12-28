from django.shortcuts import render
from django.views.generic.base import TemplateView
from school.models import School
from klass.models import Klass
from django.conf import settings

class KlassListMixin(object):
	def get_context_data(self, **kwargs):
		context=super(KlassListMixin, self).get_context_data(**kwargs)
		context['list_of_klasses']=Klass.objects.all()
		return context


class HomepageView(KlassListMixin, TemplateView):
	template_name='homepage/homepage.html'

	def get_context_data(self, **kwargs):
		context=super().get_context_data(**kwargs)
		school_name=settings.SCHOOL_NAME
		context['school']=School.objects.get(name=school_name)
		return context
		