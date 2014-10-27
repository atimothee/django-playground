from django.contrib import admin
from animalia.admin import site
from models import Movie, Director, Studio, Genre
# Register your models here.
site.register(Movie)
site.register(Director)
site.register(Genre)
site.register(Studio)