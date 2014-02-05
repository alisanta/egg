from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse,reverse_lazy
from django.views import generic


from employee.models import Employee,EmployeeForm
# Create your views here.
class IndexView(generic.ListView):
	template_name = 'employee/index.html'
	context_object_name = 'emp_list'
	emp_list = Employee.objects.all()

	#paginator = Paginator(emp_list, 3)
	paginate_by = 5
	

	def get_queryset(self):
		return Employee.objects.order_by('firstname')

class viewEmployee(generic.DetailView):
	"""docstring for viewEmployee"""
	template_name = "employee/view_employee.html"
	model = Employee

class editEmployee(generic.UpdateView):
	"""docstring for editEmployee"""
	template_name = "employee/edit_employee.html"
	form_class= EmployeeForm
	model = Employee
	fields = ['department']
	context_object_name = 'emp'
	#def form_valid(self, form):
		# This method is called when valid form data has been POSTed.
		# It should return an HttpResponse.
	#	saveflag  = form.save()
	#	return HttpResponseRedirect('/employee/')
		

class viewEmployeeDepartment(generic.ListView):
	"""docstring for viewEmployeeDepartment"""
	template_name = 'employee/index.html'
	context_object_name = 'emp_list'
	
	def get_queryset(self):
		return Employee.objects.order_by('department')

	

class createEmployee(generic.CreateView):
	"""docstring for createEmployee"""
	model=Employee
	template_name = 'employee/new_employee_old.html'
	
	#success_url = reverse_lazy('employee:index')

'''
def newemployee(request):
	if request.method =='POST':
		form= EmployeeForm(request.POST)
		if form.is_valid():
			#save
			saveflag  = form.save()
			return HttpResponseRedirect('/employee/')
	else:
		form=EmployeeForm()

	return render(request, 'employee/new_employee.html', {
		'form':form,
		})
'''