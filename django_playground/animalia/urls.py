__author__ = 'Timo'

from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import AnimalDetail

urlpatterns = patterns('',

    url(r'^$', 'animalia.views.home', name='home'),
    url(r'^animals/list$', 'animalia.views.animal_list'),
    url(r'^id/(?P<pk>[-_\w]+)/$', AnimalDetail.as_view()),
)