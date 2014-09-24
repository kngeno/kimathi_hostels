from django.conf.urls import patterns, include, url
#from django.conf import settings

urlpatterns = patterns('',    
    url(r'^$', 'hostels.views.home', name='home'),
    url(r'^info/$', 'hostels.views.info', name='info'),
    url(r'^map/get-hostels/$', 'hostels.views.get_hostels', name='get-hostels'),
    url(r'^map/hostels/filter/$', 'hostels.views.hostels_filter', name='hostels_filter'),
)

#Heroku Deployment
'''
urlpatterns += patterns('',
    (r'^' + settings.STATIC_URL[1:] + '(?P.*)$', 'django.views.static.serve',
         {'document_root': settings.STATIC_ROOT}),)
'''