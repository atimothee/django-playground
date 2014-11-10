from django.shortcuts import render_to_response
from models import Movie
from django.views.generic import DetailView
from django.http import Http404
from django.db.models import F
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from forms import MovieForm, ActorForm, GenreForm, DirectorForm, WriterForm

def home(request):
    movies_list = Movie.objects.filter(is_featured=True)
    paginator = Paginator(movies_list, 6)
    page = request.GET.get('page')
    try:
        movies = paginator.page(page)
    except PageNotAnInteger:
        movies = paginator.page(1)
    except EmptyPage:
        movies = paginator.page(paginator.num_pages)
    return render_to_response('movie_library/home.html', {'home_active':'active', 'movies': movies}, RequestContext(request))

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

@login_required
def dashboard(request):
    context = RequestContext(request)
    movies = Movie.objects.filter(uploaded_by=request.user)
    #movie_form = ProductForm()
    return render_to_response("movie_library/dashboard/dashboard.html", {'movies': movies, "movie_form": '', 'dashboard_active':'active'}, context)

@login_required
def dashboard_add_movie(request):
    context = RequestContext(request)
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.uploaded_by = request.user
            obj.save()
            return HttpResponseRedirect('/movies/dashboard')
        return render_to_response("movie_library/dashboard/add_movie.html", {"form": form, 'dashboard_active':'active'}, context)

    elif request.method == 'GET':
        form = MovieForm()
        return render_to_response("movie_library/dashboard/add_movie.html", {"form": form, 'dashboard_active':'active'}, context)

@login_required
def dashboard_add_actor(request):
    context = RequestContext(request)
    if request.method == 'POST':
        form = ActorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/movies/dashboard')
        return render_to_response("movie_library/dashboard/add_actor.html", {"form": form, 'dashboard_active':'active'}, context)

    elif request.method == 'GET':
        form = ActorForm()
        return render_to_response("movie_library/dashboard/add_actor.html", {"form": form, 'dashboard_active':'active'}, context)

@login_required
def dashboard_add_director(request):
    context = RequestContext(request)
    if request.method == 'POST':
        form = DirectorForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/movies/dashboard')
        return render_to_response("movie_library/dashboard/add_director.html", {"form": form, 'dashboard_active':'active'}, context)

    elif request.method == 'GET':
        form = DirectorForm()
        return render_to_response("movie_library/dashboard/add_director.html", {"form": form, 'dashboard_active':'active'}, context)

@login_required
def dashboard_add_writer(request):
    context = RequestContext(request)
    if request.method == 'POST':
        form = WriterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/movies/dashboard')
        return render_to_response("movie_library/dashboard/add_writer.html", {"form": form, 'dashboard_active':'active'}, context)

    elif request.method == 'GET':
        form = WriterForm()
        return render_to_response("movie_library/dashboard/add_writer.html", {"form": form, 'dashboard_active':'active'}, context)

@login_required
def dashboard_add_genre(request):
    context = RequestContext(request)
    if request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/movies/dashboard')
        return render_to_response("movie_library/dashboard/add_genre.html", {"form": form, 'dashboard_active':'active'}, context)

    elif request.method == 'GET':
        form = GenreForm()
        return render_to_response("movie_library/dashboard/add_genre.html", {"form": form, 'dashboard_active':'active'}, context)
