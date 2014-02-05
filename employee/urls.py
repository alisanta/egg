from django.conf.urls import patterns,url

from employee import views
#from employee.views import *

urlpatterns = patterns('', 
	url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^viewEmployeeDepartment/$', views.viewEmployeeDepartment.as_view(), name='viewEmployeeDepartment'),
    #url(r'^new/', views.newemployee, name='newemployee'),
    url(r'^create/', views.createEmployee.as_view(), name='createEmployee'),
	#url(r'^$', views.employee, name='employee'),
    url(r'^(?P<pk>\d+)/view$', views.viewEmployee.as_view(), name='viewEmployee'),
    url(r'^(?P<pk>\d+)/edit$', views.editEmployee.as_view(), name='editEmployee'),
    
)