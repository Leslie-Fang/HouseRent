from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.hello_poll, name='index'),#r'^$' root path, ^ corespond to the begin, $ corespond to the end,name is just for record
    url(r'^second/$', views.second_poll, name='index2'),
]