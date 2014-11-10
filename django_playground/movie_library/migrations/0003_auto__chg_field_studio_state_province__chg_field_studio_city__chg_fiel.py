# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Studio.state_province'
        db.alter_column(u'movie_library_studio', 'state_province', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Studio.city'
        db.alter_column(u'movie_library_studio', 'city', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Studio.country'
        db.alter_column(u'movie_library_studio', 'country', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Studio.address'
        db.alter_column(u'movie_library_studio', 'address', self.gf('django.db.models.fields.TextField')())
        # Deleting field 'Director.salutation'
        db.delete_column(u'movie_library_director', 'salutation')

        # Deleting field 'Director.email'
        db.delete_column(u'movie_library_director', 'email')

        # Deleting field 'Movie.release_date'
        db.delete_column(u'movie_library_movie', 'release_date')

        # Adding field 'Movie.release_year'
        db.add_column(u'movie_library_movie', 'release_year',
                      self.gf('django.db.models.fields.IntegerField')(default=0, blank=True),
                      keep_default=False)

        # Adding field 'Movie.is_featured'
        db.add_column(u'movie_library_movie', 'is_featured',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Deleting field 'Writer.salutation'
        db.delete_column(u'movie_library_writer', 'salutation')

        # Deleting field 'Writer.email'
        db.delete_column(u'movie_library_writer', 'email')


    def backwards(self, orm):

        # Changing field 'Studio.state_province'
        db.alter_column(u'movie_library_studio', 'state_province', self.gf('django.db.models.fields.CharField')(max_length=30))

        # Changing field 'Studio.city'
        db.alter_column(u'movie_library_studio', 'city', self.gf('django.db.models.fields.CharField')(max_length=60))

        # Changing field 'Studio.country'
        db.alter_column(u'movie_library_studio', 'country', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Studio.address'
        db.alter_column(u'movie_library_studio', 'address', self.gf('django.db.models.fields.CharField')(max_length=50))
        # Adding field 'Director.salutation'
        db.add_column(u'movie_library_director', 'salutation',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=10),
                      keep_default=False)

        # Adding field 'Director.email'
        db.add_column(u'movie_library_director', 'email',
                      self.gf('django.db.models.fields.EmailField')(default='', max_length=75),
                      keep_default=False)

        # Adding field 'Movie.release_date'
        db.add_column(u'movie_library_movie', 'release_date',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 11, 9, 0, 0)),
                      keep_default=False)

        # Deleting field 'Movie.release_year'
        db.delete_column(u'movie_library_movie', 'release_year')

        # Deleting field 'Movie.is_featured'
        db.delete_column(u'movie_library_movie', 'is_featured')

        # Adding field 'Writer.salutation'
        db.add_column(u'movie_library_writer', 'salutation',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=10),
                      keep_default=False)

        # Adding field 'Writer.email'
        db.add_column(u'movie_library_writer', 'email',
                      self.gf('django.db.models.fields.EmailField')(default='', max_length=75),
                      keep_default=False)


    models = {
        u'movie_library.director': {
            'Meta': {'object_name': 'Director'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'nick_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'})
        },
        u'movie_library.genre': {
            'Meta': {'object_name': 'Genre'},
            'explanation': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'movie_library.movie': {
            'Meta': {'object_name': 'Movie'},
            'cover_art': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'director': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['movie_library.Director']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'release_year': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'studio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['movie_library.Studio']"}),
            'synopsis': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'writer': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['movie_library.Writer']", 'symmetrical': 'False'})
        },
        u'movie_library.studio': {
            'Meta': {'object_name': 'Studio'},
            'address': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'state_province': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'movie_library.writer': {
            'Meta': {'object_name': 'Writer'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        }
    }

    complete_apps = ['movie_library']