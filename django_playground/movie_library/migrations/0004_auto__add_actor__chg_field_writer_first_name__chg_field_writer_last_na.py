# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Actor'
        db.create_table(u'movie_library_actor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('date_of_birth', self.gf('django.db.models.fields.DateField')(blank=True)),
        ))
        db.send_create_signal(u'movie_library', ['Actor'])

        # Adding M2M table for field actor on 'Movie'
        m2m_table_name = db.shorten_name(u'movie_library_movie_actor')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('movie', models.ForeignKey(orm[u'movie_library.movie'], null=False)),
            ('actor', models.ForeignKey(orm[u'movie_library.actor'], null=False))
        ))
        db.create_unique(m2m_table_name, ['movie_id', 'actor_id'])


        # Changing field 'Writer.first_name'
        db.alter_column(u'movie_library_writer', 'first_name', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Writer.last_name'
        db.alter_column(u'movie_library_writer', 'last_name', self.gf('django.db.models.fields.CharField')(max_length=100))

    def backwards(self, orm):
        # Deleting model 'Actor'
        db.delete_table(u'movie_library_actor')

        # Removing M2M table for field actor on 'Movie'
        db.delete_table(db.shorten_name(u'movie_library_movie_actor'))


        # Changing field 'Writer.first_name'
        db.alter_column(u'movie_library_writer', 'first_name', self.gf('django.db.models.fields.CharField')(max_length=30))

        # Changing field 'Writer.last_name'
        db.alter_column(u'movie_library_writer', 'last_name', self.gf('django.db.models.fields.CharField')(max_length=40))

    models = {
        u'movie_library.actor': {
            'Meta': {'object_name': 'Actor'},
            'date_of_birth': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
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
            'actor': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['movie_library.Actor']", 'symmetrical': 'False'}),
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
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['movie_library']