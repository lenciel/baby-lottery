from django.conf.urls import patterns, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('greeting.views',
                       url(r'^send$', 'send_greeting', name='send_greeting'),
                       url(r'^result', 'result', name='result'),
)
