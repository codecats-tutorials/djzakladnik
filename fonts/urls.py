from django.conf.urls import url, patterns, include
from fonts import views

urlpatterns = patterns('',
    url(r'^(?P<name>.+)$', views.index, name='index'),
)          