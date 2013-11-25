import httplib2
import logging
from django.conf import settings
from django.http import HttpResponse
from django.views.generic import View

logger = logging.getLogger(__name__)


class ServiceProxy(View):
    headers = dict()
    password = None
    request_base = str()
    username = None

    def get_credentials(self):
        return self.username, self.password

    def get_request_parameters(self):
        return self.request.GET.copy()

    def get_headers(self):
        return self.headers

    def proxy_request(self):
        path = self.request.get_full_path()
        headers = self.headers
        http = httplib2.Http()
        http.add_credentials(*self.get_credentials())

        resp, content = http.request(self.request_base + "?{0}".format(self.get_request_parameters().urlencode()),
                                     self.request.method, body=self.request.body, headers=headers)

        logger.debug("Service proxy response: {0}".format(resp))

        return HttpResponse(content, status=resp.status, content_type=resp.get('content-type'))


class DigitalGlobeProxy(ServiceProxy):
    username = getattr(settings, 'DG_SERVICE_USERNAME', None)
    password = getattr(settings, 'DG_SERVICE_PASSWORD', None)
    connect_id = getattr(settings, 'DG_SERVICE_CONNECTID', None)
    request_base = "https://services.digitalglobe.com/mapservice/wmsaccess"

    http_method_names = ['get']

    def get_request_parameters(self):
        params = super(DigitalGlobeProxy, self).get_request_parameters()

        logger.debug("Digital Globe Proxy Parameters: {0}".format(params))

        if not params.has_key('connectid'):
            params.update({'connectid':self.connect_id})

        if params.has_key('SRS'):
            params['SRS'] = params['SRS'].replace('900913', '3857')

        return params

    def get(self, request, *args, **kwargs):
        return self.proxy_request()
