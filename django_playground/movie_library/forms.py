__author__ = 'Timo'
from django import forms
from models import Movie, Director, Studio, Writer, Actor, Genre

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