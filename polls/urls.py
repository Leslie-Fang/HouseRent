from django.conf.urls import url

from . import views,view2

urlpatterns = [
    url(r'^$', views.hello_poll, name='hello_poll'),#r'^$' root path, ^ corespond to the begin, $ corespond to the end,name is just for record
    url(r'^second/$', views.second_poll, name='second_poll'),
    url(r'^index/$', views.index, name='index'),
    url(r'^index2/$', view2.index, name='index2'),
]