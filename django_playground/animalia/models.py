from django.db import models

class Phylum(models.Model):
    name = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name

class Class(models.Model):
    name = models.CharField(max_length=50)
    phylum = models.ForeignKey(Phylum)
    def __unicode__(self):
        return self.name

class Order(models.Model):
    name = models.CharField(max_length=50)
    classe = models.ForeignKey(Class)
    def __unicode__(self):
        return self.name

class Family(models.Model):
    name = models.CharField(max_length=50)
    order = models.ForeignKey(Order)
    def __unicode__(self):
        return self.name

class Genus(models.Model):
    name = models.CharField(max_length=50)
    family = models.ForeignKey(Family)
    def __unicode__(self):
        return self.name

class Species(models.Model):
    name = models.CharField(max_length=50)
    genus = models.ForeignKey(Genus)
    def __unicode__(self):
        return self.name

class Animal(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images", blank=True)
    description = models.TextField(blank=True)
    species = models.ForeignKey(Species)
    def __unicode__(self):
        return self.name