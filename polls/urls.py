from django.conf.urls import url

from . import views,view2


urlpatterns = [
    url(r'^$', views.hello_poll, name='hello_poll'),#r'^$' root path, ^ corespond to the begin, $ corespond to the end,name is just for record
    url(r'^second/$', views.second_poll, name='second_poll'),
    url(r'^index/$', views.index, name='index'),
    url(r'^index2/$', view2.index, name='index2'),
    url(r'^(?P<question_id>[0-9]+)/$', views.question_detail, name='detail'),
    url(r'^create_question/$', views.create_question, name='create_question'),
    url(r'^create_now/$', views.create_now, name='create_now'),
    #?P<question_id> pass the parameter into the question_id
    #.* regular expression
    url(r'^create_q_wname/(?P<question_id>.*)/$', views.create_q_wname, name='create_q_wname'),


]