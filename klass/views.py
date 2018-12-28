from django.shortcuts import render
from homepage.views import KlassListMixin
from django.views.generic.edit import CreateView
from .models import Klass

class CreateKlassView(KlassListMixin, CreateView):
	model=Klass
	fields=['teacher','room_num','class_name',]
	template_name='klass/add_klass_form.html'
	

# class KlassCreateView(KlassListMixin, CreateView):
#     model=Klass
#     form_class=KlassForm
#     template_name='classlists/add_klass_form.html'
#     
#     def form_valid(self, form):
#         new_klass=form.save()
#         school_schedule=SchoolScheduleDetails.objects.get(name=settings.SCHOOL_NAME)
#         slot_length=school_schedule.slot_length
#         
#         ##Create PM Slots for a Class
#         slot_start=school_schedule.pm_start
#         for i in range(0,school_schedule.num_pm_slots):
#             slot_end=(datetime.combine(date.today(), slot_start)+timedelta(minutes=slot_length)).time()
#             new_slot=Slot.objects.create(klass=new_klass,
#                                          start=slot_start,
#                                          end=slot_end,
#                                          am_pm='pm',
#                                          not_available=False)
#             slot_start=slot_end
# 
#         ##Create PM Slots for a Class
#         slot_start=school_schedule.am_start
#         for i in range(0,school_schedule.num_am_slots):
#             slot_end=(datetime.combine(date.today(), slot_start)+timedelta(minutes=slot_length)).time()
#             new_slot=Slot.objects.create(klass=new_klass,
#                                          start=slot_start,
#                                          end=slot_end,
#                                          am_pm='am',
#                                          not_available=False)
#             slot_start=slot_end
# 
#         return HttpResponseRedirect(reverse_lazy('homepage-view'))