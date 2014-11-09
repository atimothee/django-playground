from django.shortcuts import render_to_response
from models import Animal
from django.views.generic import DetailView
from django.http import Http404
from django.db.models import F
from django.template import RequestContext

def home(request):
    return render_to_response('animalia/home.html', {'popular': Animal.objects.all().order_by("views")[:5]}, RequestContext(request))

def animal_list(request):
    animals = Animal.objects.filter(name__icontains=request.GET.get('name', ''), species__genus__family__name__icontains=request.GET.get('family', ''))
    return render_to_response('animalia/animal_list.html', {'animals': animals})

class AnimalDetail(DetailView):
    model = Animal
    template_name = 'animalia/animal_detail.html'
    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg, None)
        try:
            Animal.objects.filter(pk=pk).update(views=F('views')+1)
            return Animal.objects.get(pk=pk)
        except Animal.DoesNotExist:
            raise Http404