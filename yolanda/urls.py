from django.conf.urls import patterns, url, include
from geonode.urls import urlpatterns

urlpatterns = patterns('',
    (r'^services/', include('yolanda.services.urls')),
    url(r'^$', 'geonode.views.index', {'template': 'site_index.html'}, name='home'),
 ) + urlpatterns
