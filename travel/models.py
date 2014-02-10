from django.db import models
from django.forms import ModelForm 
from datetime import date
from django.core.urlresolvers import reverse

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, Column, Button, Div, Field, MultiField, HTML
from crispy_forms.bootstrap import ( AppendedText,
    PrependedText, PrependedAppendedText, FormActions)


# Create your models here.
class TRAVELREQUEST(models.Model):
	request_number = models.CharField(max_length=10, blank=True, null=True)
	request_date = models.DateField(default=date.today)
	requestor_name = models.CharField("",max_length=30)

	purpose = models.TextField()
	destination = models.CharField(max_length=30)
	date_departure = models.DateTimeField("Date of Departure")
	date_return = models.DateTimeField("Date of Return")

	days_fullday = models.IntegerField("",null=True)
	days_halfday = models.IntegerField("",null=True)
	days_breakfast = models.IntegerField("",null=True)
	days_lunch = models.IntegerField("",null=True)
	days_dinner = models.IntegerField("",null=True)


	rate_fullday = models.DecimalField("",max_digits=6, decimal_places=2, null=True)
	rate_halfday = models.DecimalField("",max_digits=6, decimal_places=2, null=True)
	rate_breakfast = models.DecimalField("",max_digits=6, decimal_places=2, null=True)
	rate_lunch = models.DecimalField("",max_digits=6, decimal_places=2, null=True)
	rate_dinner = models.DecimalField("",max_digits=6, decimal_places=2, null=True)


	amount_fullday = models.DecimalField("",max_digits=6, decimal_places=2,null=True)
	amount_halfday = models.DecimalField("",max_digits=6, decimal_places=2, null=True)
	amount_breakfast = models.DecimalField("",max_digits=6, decimal_places=2, null=True)
	amount_lunch = models.DecimalField("",max_digits=6, decimal_places=2, null=True)
	amount_dinner = models.DecimalField("",max_digits=6, decimal_places=2,null=True)

	total_request_amount = models.DecimalField(max_digits=8, decimal_places=2, null=True)

	emp_name = models.CharField("Employee Name", max_length=30)
	emp_division = models.CharField("Division", max_length=10)
	emp_location = models.CharField("Location", max_length=20)
	emp_jobtitle = models.CharField("Job Title",max_length=30)

	def get_absolute_url(self):
		return reverse('travel:index')

class TRAVELREQUESTFORM(ModelForm):

	error_css_class = 'error'
	required_css_class = 'required'
	class Meta:
		model = TRAVELREQUEST
		#exclude = ['request_date', 'request_number']
	def __init__(self, *args, **kwargs):
		super(TRAVELREQUESTFORM, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'POST'
		#self.helper.form_action = "/travel/create/"
		self.helper.form_class = 'form-horizontal'
		self.helper.label_class = 'col-sm-4'
		self.helper.field_class = 'col-sm-8'
		self.helper.form_tag = False # do not render form tag, so we can differentiate edit vs new
		#self.helper.form_show_labels = False 
		self.helper.layout = Layout(
		

		Fieldset(
			'Travel Expense Claim Form',
			Div(Div(Field('request_number'),css_class="col-md-6"),css_class="row-fluid col-md-12"),
			Div(Div(Field('request_date'),css_class="col-md-6"),css_class="row-fluid col-md-12"),
			
			Div(
				Div('emp_name',css_class=" col-md-6"),
				Div('emp_division',css_class="col-md-6"),
				Div('emp_location',css_class="col-md-6"),
				Div('emp_jobtitle',css_class="col-md-6"),
				css_class="row-fluid col-md-12",
				style="background-color:#eee; padding:5px;"
			),
			
			Div(Div(Field('purpose',rows=3),css_class="col-md-6"),css_class="row-fluid col-md-12"),
			Div(Div('destination',css_class="col-md-6"),css_class="row-fluid col-md-12"),
			Div(Div('date_departure',css_class="col-md-6"),css_class="row-fluid col-md-12"),
			Div(Div('date_return',css_class="col-md-6"),css_class="row-fluid col-md-12"),
			HTML('<div class="row-fluid col-md-12" style="background-color:#eee; border:1px solid; padding:5px;"><div class="col-md-4 ">Number of Days</div><div class="col-md-4 ">Rate</div><div class="col-md-4 ">Amount</div>'),
			
			
			Column('days_fullday','days_halfday','days_breakfast','days_lunch','days_dinner',css_class="row-fluid col-md-3"),
			Column('rate_fullday','rate_halfday','rate_breakfast','rate_lunch','rate_dinner',css_class="row-fluid col-md-3"),
			Column('amount_fullday','amount_halfday','amount_breakfast','amount_lunch','amount_dinner',css_class="row-fluid col-md-3"),
			HTML('</div>'),
			Div(Div('total_request_amount',css_class="col-md-6"),css_class="row-fluid col-md-12"),

			HTML('<table class="table table-bordered"><tr><td class="success">Requestor</td><td class="success">Section Head</td><td class="success">General Manager</td><td class="success"></td></tr>'),
			HTML('<tr><td style="height:100px;">'),
			Field('requestor_name'),
			HTML('</td><td></td><td></td><td></td></tr>'),
			HTML('<tr><td class="success">Account Supervisor</td><td class="success">Financial Controller</td><td class="success">CEO</td><td class="success">Accountant</td></tr>'),
			HTML('<tr><td style="height:100px;">&nbsp;<br/>&nbsp;</td><td></td><td></td><td></td></tr>'),
			HTML('</table>'),
			css_class="form-group "
		),
		

		
		
		)

form = TRAVELREQUESTFORM()

    