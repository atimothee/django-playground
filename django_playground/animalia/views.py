from django.shortcuts import render_to_response
from animalia.models import Animal
from django.views.generic import DetailView

def home(request):
    return render_to_response('animalia/home.html', {})

def animal_list(request):
    animals = Animal.objects.filter(name__icontains=request.GET.get('name', ''), species__genus__family__name__icontains=request.GET.get('family', ''))
    return render_to_response('animalia/animal_list.html', {'animals': animals})

class AnimalDetail(DetailView):
    model = Animal
    template_name = 'animalia/animal_detail.html'