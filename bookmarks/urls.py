from django.conf.urls import url, patterns, include
from bookmarks import views
from django.contrib.auth.views import login, logout

urlpatterns = patterns('',
    url(r'^$', views.index, name = 'index'),
    url(r'^subscribe-(?P<id>[0-9]+)/$', views.subscribe, name = 'subscribe'),
    url(r'^unsubscribe-(?P<id>[0-9]+)/$', views.unsubscribe, name = 'unsubscribe'),
    url(r'^my/$', views.my, name = 'my'),
    url(r'^add/$', views.add, name = 'add'),
    url(r'^login/$', login, name = 'login'),
    url(r'^logout/$', logout , name = 'logout'),
    url(r'^registration/$', views.registration, name = 'registration'),
)