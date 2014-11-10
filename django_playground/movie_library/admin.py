from django.contrib import admin
from animalia.admin import site
from models import Movie, Director, Studio, Genre
# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    # list_display = (
    #      'file_type', 'category', 'keywords', 'xlarge_graphic',
    #     'caption')

    exclude = ('uploaded_by',)

    search_fields = ['title', 'genre__name',]

    #actions = [verify_product, make_free]

    #list_filter = ('category', 'file_type', 'is_verified', 'uploaded_by')

    list_select_related = ('genre', 'studio')

    # view_on_site = True

    def save_model(self, request, obj, form, change):
        if not change:
            obj.uploaded_by = request.user
            obj.save()
        else:
            super(MovieAdmin, self).save_model(request, obj, form, change)

site.register(Movie, MovieAdmin)
site.register(Director)
site.register(Genre)
site.register(Studio)