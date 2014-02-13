from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse,reverse_lazy
from django.views import generic

from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.shortcuts import render_to_response

from travel.models import TRAVELREQUEST, TRAVELREQUESTFORM
# Create your views here.


def user_login(request):
	context = RequestContext(request)
	# If the request is a HTTP POST, try to pull out the relevant information.
	if request.method == 'POST':
		# Gather the username and password provided by the user.
		# This information is obtained from the login form.
		username = request.POST['username']
		password = request.POST['password']

		# Use Django's machinery to attempt to see if the username/password
		# combination is valid - a User object is returned if it is.
		user = authenticate(username=username, password=password)

		# If we have a User object, the details are correct.
		# If None (Python's way of representing the absence of a value), no user
		# with matching credentials was found.
		if user is not None:
			# Is the account active? It could have been disabled.
			if user.is_active:
				# If the account is valid and active, we can log the user in.
				# We'll send the user back to the homepage.
				login(request, user)
				return HttpResponseRedirect('/travel/')
			else:
				# An inactive account was used - no logging in!
				return HttpResponse("Your Rango account is disabled.")
		else:
			# Bad login details were provided. So we can't log the user in.
			print "Invalid login details: {0}, {1}".format(username, password)
			return HttpResponse("Invalid login details supplied.")

	# The request is not a HTTP POST, so display the login form.
	# This scenario would most likely be a HTTP GET.
	else:
		# No context variables to pass to the template system, hence the
		# blank dictionary object...
		return render_to_response('login2.html', {}, context)

def logout_view(request):
    logout(request)



class IndexView(generic.ListView):
	template_name = 'index.html'
	context_object_name = 'doc_list'
	doc_list = TRAVELREQUEST.objects.all()
	model = TRAVELREQUEST
	paginate_by = 10
	
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
	template_name = 'edit_request.html'
	form_class= TRAVELREQUESTFORM
	model = TRAVELREQUEST
	
	success_url = reverse_lazy('travel:index')