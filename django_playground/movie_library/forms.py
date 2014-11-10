__author__ = 'Timo'
from django import forms
from models import Movie, Director, Studio, Writer, Actor, Genre

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        exclude = ('uploaded_by',)
    def save_model(self, request, obj, form, change):
        if not change:
            obj.uploaded_by = request.user
            obj.save()
        else:
            super(MovieForm, self).save_model(request, obj, form, change)

class WriterForm(forms.ModelForm):
    class Meta:
        model = Writer

class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director

class ActorForm(forms.ModelForm):
    class Meta:
        model = Actor