from django.conf.urls import patterns, include, url


urlpatterns = patterns('',    
    url(r'^$', 'hostels.views.home', name='home'),
    url(r'^info/$', 'hostels.views.info', name='info'),
    url(r'^map/get-hostels/$', 'hostels.views.get_hostels', name='get-hostels'),
    url(r'^map/hostels/filter/$', 'hostels.views.hostels_filter', name='hostels_filter'),
)
