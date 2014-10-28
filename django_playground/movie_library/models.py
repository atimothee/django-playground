from django.db import models

# Create your models here.
class Studio(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

class Genre(models.Model):
    name = models.CharField(max_length=50)
    explanation = models.TextField(blank=True)

class Writer(models.Model):
    salutation = models.CharField(max_length=10)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()

class Director(models.Model):
    salutation = models.CharField(max_length=10)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    nick_name = models.CharField(max_length=30)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    writer = models.ManyToManyField(Writer)
    director = models.ManyToManyField(Director)
    synopsis = models.TextField(blank=True)
    studio = models.ForeignKey(Studio)
    release_date = models.DateField()
    headshot = models.ImageField(upload_to='/cover_art')