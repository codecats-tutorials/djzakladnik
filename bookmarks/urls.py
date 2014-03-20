from django.conf.urls import url, patterns, include
from bookmarks import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)