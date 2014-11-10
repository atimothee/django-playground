from django.shortcuts import render_to_response
from models import Animal
from django.views.generic import DetailView
from django.http import Http404
from django.db.models import F
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
    animals_list = Animal.objects.all().order_by("views")[:5]
    paginator = Paginator(animals_list, 6)
    page = request.GET.get('page')
    try:
        animals = paginator.page(page)
    except PageNotAnInteger:
        animals = paginator.page(1)
    except EmptyPage:
        animals = paginator.page(paginator.num_pages)
    return render_to_response('animalia/home.html', {'popular': animals, 'home_active': 'active'}, RequestContext(request))

def animal_list(request):
    animals = Animal.objects.filter(name__icontains=request.GET.get('name', ''), species__genus__family__name__icontains=request.GET.get('family', ''))
    return render_to_response('animalia/animal_list.html', {'animals': animals, 'catalogue_active':'active'})

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
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        pk = self.kwargs.get(self.pk_url_kwarg, None)
        obj = Animal.objects.get(pk=pk)
        context = super(AnimalDetail, self).get_context_data(**kwargs)
        context['related'] = Animal.objects.filter(species__genus__family_id=obj.species.genus.family_id)[:3]  # #look into proper filter using ORs
        return context