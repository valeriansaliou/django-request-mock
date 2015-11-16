import sys

if sys.version_info >= (3, ):
    from urllib.parse import urlparse
    from io import StringIO
else:
    from urlparse import urlparse
    from StringIO import StringIO


from django.conf import settings
from django.core.handlers.wsgi import WSGIRequest
from django.contrib.auth.models import AnonymousUser


def request_mock(base=settings.SITE_URL, path='/', query_string='', user=None):
    """
    Create a request object that mocks a real one
    Useful in case a real request object is not available, but is needed (delayed Celery tasks for instance)
    """
    url_parse = urlparse(base)

    request = WSGIRequest({
        'REQUEST_METHOD': 'GET',
        'REQUEST_URI': path,

        'PATH_INFO': path,
        'QUERY_STRING': query_string,
        'SCRIPT_NAME': '',
        'HTTPS': ('on' if url_parse.scheme == 'https' else 'off'),

        'HTTP_ACCEPT': '*/*',
        'HTTP_HOST': url_parse.hostname,
        'HTTP_REFERER': base,
        'HTTP_USER_AGENT': 'MockRequest/1.0',
        'HTTP_ACCEPT_LANGUAGE': 'en-US,en;q=0.8',

        'SERVER_PROTOCOL': 'HTTP/1.1',
        'SERVER_NAME': url_parse.hostname,
        'SERVER_PORT': url_parse.port or (443 if url_parse.scheme == 'https' else 80),

        'wsgi.input': StringIO(),
        'wsgi.multiprocess': True,
        'wsgi.multithread': False,
        'wsgi.run_once': False,
        'wsgi.url_scheme': url_parse.scheme or 'http',
        'wsgi.version': (1, 0),
    })
    
    request.user = AnonymousUser() if user is None else user
    request.session = {}
    
    return request
