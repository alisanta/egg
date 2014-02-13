from django.conf.urls import patterns,url
from django.contrib.auth.views import login
from travel import views
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('', 
	url(r'^$', login_required(views.IndexView.as_view()), name='index'),
    url(r'^create/', views.createTravel.as_view(), name='createTravel'),
    url(r'^(?P<pk>\d+)/view$', views.viewTravel.as_view(), name='viewTravel'),
    url(r'^(?P<pk>\d+)/edit$', views.editTravel.as_view(), name='editTravel'),
    #url(r'^account/login/$', views.user_login, name='login'),
    url(r'^accounts/login/', 'django.contrib.auth.views.login',{'template_name': 'login2.html'},  name='mylogin'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', name='mylogout'),
)