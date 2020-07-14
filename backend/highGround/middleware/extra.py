from django.utils.deprecation import MiddlewareMixin


class LogVariablesMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request.log_extra = {
            'clientip': request.META['REMOTE_ADDR'],
            'user': request.user
        }