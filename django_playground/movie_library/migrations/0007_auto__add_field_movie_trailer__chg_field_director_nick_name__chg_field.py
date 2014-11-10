# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Movie.trailer'
        db.add_column(u'movie_library_movie', 'trailer',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=200, blank=True),
                      keep_default=False)


        # Changing field 'Director.nick_name'
        db.alter_column(u'movie_library_director', 'nick_name', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Director.first_name'
        db.alter_column(u'movie_library_director', 'first_name', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Director.last_name'
        db.alter_column(u'movie_library_director', 'last_name', self.gf('django.db.models.fields.CharField')(max_length=100))

    def backwards(self, orm):
        # Deleting field 'Movie.trailer'
        db.delete_column(u'movie_library_movie', 'trailer')


        # Changing field 'Director.nick_name'
        db.alter_column(u'movie_library_director', 'nick_name', self.gf('django.db.models.fields.CharField')(max_length=30))

        # Changing field 'Director.first_name'
        db.alter_column(u'movie_library_director', 'first_name', self.gf('django.db.models.fields.CharField')(max_length=30))

        # Changing field 'Director.last_name'
        db.alter_column(u'movie_library_director', 'last_name', self.gf('django.db.models.fields.CharField')(max_length=40))

    models = {
        u'movie_library.actor': {
            'Meta': {'object_name': 'Actor'},
            'date_of_birth': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        u'movie_library.director': {
            'Meta': {'object_name': 'Director'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'nick_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        u'movie_library.genre': {
            'Meta': {'object_name': 'Genre'},
            'explanation': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'movie_library.movie': {
            'Meta': {'object_name': 'Movie'},
            'actor': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['movie_library.Actor']", 'symmetrical': 'False'}),
            'cover_art': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'director': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['movie_library.Director']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'release_year': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'studio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['movie_library.Studio']", 'null': 'True', 'blank': 'True'}),
            'synopsis': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'trailer': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
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
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['movie_library']