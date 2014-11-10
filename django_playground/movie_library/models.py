from django.db import models

# Create your models here.
class Studio(models.Model):
    name = models.CharField(max_length=30)
    address = models.TextField(blank=True)
    city = models.CharField(max_length=100, blank=True)
    state_province = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    website = models.URLField(blank=True)
    def __unicode__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=50)
    explanation = models.TextField(blank=True)
    def __unicode__(self):
        return self.name

class Writer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    def __unicode__(self):
        return self.first_name+" "+self.last_name

class Actor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    def __unicode__(self):
        return self.first_name+" "+self.last_name

class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    nick_name = models.CharField(max_length=100, blank=True)
    def __unicode__(self):
        return self.first_name+" "+self.last_name

class Movie(models.Model):
    title = models.CharField(max_length=100)
    writer = models.ManyToManyField(Writer)
    actor = models.ManyToManyField(Actor)
    director = models.ManyToManyField(Director)
    synopsis = models.TextField(blank=True)
    studio = models.ForeignKey(Studio, blank=True, null=True)
    release_year = models.IntegerField(blank=True)
    cover_art = models.ImageField(upload_to='cover_art')
    is_featured = models.BooleanField(default=False)
    def __unicode__(self):
        return self.title