__author__ = 'Timo'
from django import forms
from models import Movie, Director, Studio, Writer, Actor, Genre, Rating
import django_filters
from django_filters.widgets import LinkWidget

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        exclude = ('uploaded_by',)

class WriterForm(forms.ModelForm):
    class Meta:
        model = Writer

class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director

class ActorForm(forms.ModelForm):
    class Meta:
        model = Actor

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre

class MovieFilter(django_filters.FilterSet):
    genre = django_filters.ModelChoiceFilter(queryset=Genre.objects.all(), widget=LinkWidget)
    director = django_filters.ModelChoiceFilter(queryset=Director.objects.all(), widget=LinkWidget)
    actor = django_filters.ModelChoiceFilter(queryset=Actor.objects.all(), widget=LinkWidget)
    rating = django_filters.ModelChoiceFilter(queryset=Rating.objects.all(), widget=LinkWidget)
    writer = django_filters.ModelChoiceFilter(queryset=Writer.objects.all(), widget=LinkWidget)
    studio = django_filters.ModelChoiceFilter(queryset=Studio.objects.all(), widget=LinkWidget)
    class Meta:
        model = Movie
        fields = ['genre', 'director', 'actor', 'writer', 'rating', 'studio']