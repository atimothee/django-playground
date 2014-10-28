from django.contrib import admin
from animalia.models import Animal, Phylum, Order, Family, Genus, Species, Class

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

