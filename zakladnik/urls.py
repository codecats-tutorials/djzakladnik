from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^', include('bookmarks.urls', namespace = 'bookmarks')),
    url(r'^fonts/', include('fonts.urls', namespace = 'fonts')),
    url(r'^admin/', include(admin.site.urls)),
)
