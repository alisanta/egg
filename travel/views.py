from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse,reverse_lazy
from django.views import generic

from travel.models import TRAVELREQUEST, TRAVELREQUESTFORM
# Create your views here.
class IndexView(generic.ListView):
	template_name = 'index.html'
	context_object_name = 'doc_list'
	doc_list = TRAVELREQUEST.objects.all()
	model = TRAVELREQUEST
	#queryset = BlogPost.objects.filter(published=True)
	#def get_queryset(self):
		# filter readers field here

class viewTravel(generic.DetailView):
	"""docstring for viewEmployee"""
	template_name = "view_request.html"
	context_object_name = 'doc'
	model = TRAVELREQUEST
	form_class= TRAVELREQUESTFORM

class createTravel(generic.CreateView):
	"""docstring for createTravel"""
	model=TRAVELREQUEST
	form_class= TRAVELREQUESTFORM

	template_name = 'new_request.html'
	success_url = reverse_lazy('travel:index')

class editTravel(generic.UpdateView):
	"""docstring for editEmployee"""
	template_name = 'new_request.html'
	form_class= TRAVELREQUESTFORM
	model = TRAVELREQUEST
	
	success_url = reverse_lazy('travel:index')