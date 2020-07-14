from django.urls import reverse
from django.http import Http404
import logging
log = logging.getLogger(__name__)


class SiteMiddleWare:

    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):
        response = self.get_response(request)
        if request.path.startswith(reverse('admin:index')):
            return response
        domain_parts = request.get_host().split('.')
        if len(domain_parts) > 2:
            subdomain = domain_parts[0]
            if subdomain.lower() == 'www':
                subdomain = None
            domain = '.'.join(domain_parts[1:])
        else:
            subdomain = None
            domain = request.get_host()
        if hasattr(response, 'data'):
            response.data['subdomain'] = subdomain
            response.data['domain'] = domain
        from apps.mainsite.app_models.sites import Site
        try:
            if hasattr(response, 'data'):
                response.data['site'] = Site.objects.get(is_active=True)
            return response
            log.info(f'{request}')
        except Site.MultipleObjectsReturned as e:
            log.error(f'{request}')
            raise Http404

