from django.conf.urls import patterns, url, include
from django.conf import settings
from django.contrib import admin
from django.http import HttpResponse

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^robots\.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: /", mimetype="text/plain")),
                       url(r'^$', 'views.home', name='home'),
                       url(r'^greeting/', include('greeting.urls', namespace='greeting')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
                            url(r'^media/(?P<path>.*)$',
                                'django.views.static.serve',
                                {'document_root': settings.MEDIA_ROOT}), )
