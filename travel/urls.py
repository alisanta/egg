from django.conf.urls import patterns,url

from travel import views


urlpatterns = patterns('', 
	url(r'^$', views.IndexView.as_view(), name='index'),
    #url(r'^viewEmployeeDepartment/$', views.viewEmployeeDepartment.as_view(), name='viewEmployeeDepartment'),
    #url(r'^new/', views.newemployee, name='newemployee'),
    url(r'^create/', views.createTravel.as_view(), name='createTravel'),
	#url(r'^$', views.employee, name='employee'),
    url(r'^(?P<pk>\d+)/view$', views.viewTravel.as_view(), name='viewTravel'),
    url(r'^(?P<pk>\d+)/edit$', views.editTravel.as_view(), name='editTravel'),
    
)