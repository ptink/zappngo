from django.http import HttpResponse
from django.conf.urls import url

DEBUG = True
ROOT_URLCONF = 'pico_django'
ALLOWED_HOSTS = '*'
DATABASES = {'default': {}}


def index(request, name):
    return HttpResponse('Hello {name}!'.format(name=(name or 'World')))

urlpatterns = [
    url(r'^(?P<name>\w+)?$', index)
]

SECRET_KEY = "not so secret"

# deploy with
# `$ zappa deploy dev`
