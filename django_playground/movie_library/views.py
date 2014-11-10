from django.shortcuts import render_to_response
from models import Movie
from django.views.generic import DetailView
from django.http import Http404
from django.db.models import F
from django.template import RequestContext

def home(request):
    return render_to_response('movie_library/home.html', {'home_active':'active', 'movies': Movie.objects.all()[:5]}, RequestContext(request))

def movie_list(request):
    return render_to_response('movie_library/movie_list.html', {'movies_active':'active'})

def movie_directors(request):
    #directors = Director
    return render_to_response('movie_library/directors.html', {'directors_active':'active'})

class MovieDetail(DetailView):
    model = Movie
    template_name = 'movie_library/movie_detail.html'
    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg, None)
        try:
            Movie.objects.filter(pk=pk)
            return Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            raise Http404
def my_404_view(request):
    return render_to_response('movie_library/404.html', {}, RequestContext(request))

def my_403_view(request):
    return render_to_response('movie_library/403.html', {}, RequestContext(request))

def my_500_view(request):
    return render_to_response('movie_library/500.html', {}, RequestContext(request))