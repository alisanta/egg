from django.db import models
from django.forms import ModelForm 
from django.core.urlresolvers import reverse

DEPT_CHOICES = (
    ('IT', 'IT.'),
    ('FIN', 'Finance.'),
    ('MKT', 'Marketing.'),
)
# Create your models here.
class Employee(models.Model):
	firstname = models.CharField(max_length=20)

	lastname = models.CharField(max_length=20)
	birthday = models.DateField(blank=True, null=True)
	department = models.CharField(max_length=50,choices=DEPT_CHOICES)
	jobtitle = models.CharField(max_length=40,help_text="")
	def get_absolute_url(self):
		return reverse('employee:index')
	def __unicode__(self):
		return (self.firstname + " "+ self.lastname)

    

class EmployeeForm(ModelForm):
	class Meta:
		model = Employee

form = EmployeeForm()
#form.as_table()
    