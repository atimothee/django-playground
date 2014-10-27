from django.contrib import admin
from animalia.models import Animal, Phylum, Order, Family, Genus, Species, Class
from movie_library.models import Movie, Director, Studio, Genre, Writer

class CustomAdminSite(admin.sites.AdminSite):
    site_header = "Playground Administration"
    site_title = "Playground site admin"

class AnimalAdmin(admin.ModelAdmin):
    exclude = ['views', 'admin_notes']

site = CustomAdminSite()

site.register(Animal, AnimalAdmin)
site.register(Phylum)
site.register(Class)
site.register(Order)
site.register(Family)
site.register(Genus)
site.register(Species)

site.register(Movie)
site.register(Writer)
site.register(Director)
site.register(Genre)
site.register(Studio)