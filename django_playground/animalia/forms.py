__author__ = 'Timo'
import django_filters
from models import Animal, Family, Phylum
from django_filters.widgets import LinkWidget

class AnimalFilter(django_filters.FilterSet):
    #name = django_filters.CharFilter(label="Search")
    #PRICE_CHOICES = (('10', '10'), ('20', '20'), ('50', '50'))
    #price = django_filters.ChoiceFilter(label="Price < ", choices=PRICE_CHOICES, widget=LinkWidget, lookup_type='lt')
    #price = django_filters.NumberFilter(lookup_type='lt')
    #created_at = django_filters.DateRangeFilter(label="Recency", widget=LinkWidget)
    #category = django_filters.ChoiceFilter(widget=LinkWidget)
    family = django_filters.ModelChoiceFilter(queryset=Family.objects.all(), widget=LinkWidget)
    pyhlum = django_filters.ModelChoiceFilter(queryset=Phylum.objects.all(), widget=LinkWidget)
    class Meta:
        model = Animal
        fields = ['species',]
