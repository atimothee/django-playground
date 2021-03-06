__author__ = 'Timo'

from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import MovieDetail

urlpatterns = patterns('',

    url(r'^$', 'movie_library.views.home', name='home'),
    url(r'^list$', 'movie_library.views.movie_list'),
    url(r'^id/(?P<pk>[-_\w]+)/$', MovieDetail.as_view()),
    url(r'^directors$', 'movie_library.views.movie_directors'),
    (r'^dashboard/$', 'movie_library.views.dashboard'),
    (r'^dashboard/add/movie$', 'movie_library.views.dashboard_add_movie'),
    (r'^dashboard/add/director$', 'movie_library.views.dashboard_add_director'),
    (r'^dashboard/add/writer$', 'movie_library.views.dashboard_add_writer'),
    (r'^dashboard/add/actor$', 'movie_library.views.dashboard_add_actor'),
    (r'^dashboard/add/genre$', 'movie_library.views.dashboard_add_genre'),
)