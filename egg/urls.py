from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'egg.views.home', name='home'),
    url(r'^employee/', include('employee.urls', namespace="employee")),
    url(r'^travel/', include('travel.urls', namespace="travel")),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login',{'template_name': 'login2.html'},  name='mylogin'),

    url(r'^admin/', include(admin.site.urls)),
)
