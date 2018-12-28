from django.urls import path
from .views import CreateKlassView

urlpatterns = [
	path('class/', CreateKlassView.as_view(), name='klass-create-view'),
]
