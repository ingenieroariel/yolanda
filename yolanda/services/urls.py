from django.conf.urls.defaults import patterns, url
from yolanda.services.views import DigitalGlobeProxy

urlpatterns = patterns("yolanda.services.views",
    url(r"^dg/?", DigitalGlobeProxy.as_view(), name="dg_service"),
)
