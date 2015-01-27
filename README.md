Django Request Mock
===================

[![Gitter](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/valeriansaliou/django-request-mock?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

Django Request Mock is an helper that allows you to generate synthetic request objects that mimic a real one, generated after a real request is being received by the framework.

Useful when coding in an HTTP isolated environment, which prevents you from accessing the request object, such as a cron method or a Celery task. This allows you to render templates and build absolute URIs from such contexts, for instance.

The request object is generated using your settings, and by default contains all the values of a request being sent to your website's default domain, using the SITE_URL configuration variable (can be of that form: https://example.com/)

## Configuration

* Ensure `SITE_URL` is defined in your **settings.py**, with a value such as 'https://example.com/'

* When you need to generate a request mock object, simply use the following code:

```python
from request_mock import request_mock

# Generate the mock object
# request_mock(base, path, user) where each argument is optional
request = request_mock()

# Can also be
request = request_mock(
    base='https://other.org/',
    path='/some/path/for/mock/request/',
    user=User.objects.get(username='dummy.user')
)
```

* All done!
