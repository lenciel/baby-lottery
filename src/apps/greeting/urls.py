from django.conf.urls import patterns, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('greeting.views',
                       url(r'^message/send$', 'send_message', name='send_message'),
)
