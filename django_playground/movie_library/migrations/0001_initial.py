# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Studio'
        db.create_table(u'movie_library_studio', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('state_province', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'movie_library', ['Studio'])

        # Adding model 'Genre'
        db.create_table(u'movie_library_genre', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('explanation', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'movie_library', ['Genre'])

        # Adding model 'Writer'
        db.create_table(u'movie_library_writer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('salutation', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('headshot', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True)),
        ))
        db.send_create_signal(u'movie_library', ['Writer'])

        # Adding model 'Director'
        db.create_table(u'movie_library_director', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('salutation', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('nick_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('headshot', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True)),
        ))
        db.send_create_signal(u'movie_library', ['Director'])

        # Adding model 'Movie'
        db.create_table(u'movie_library_movie', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('synopsis', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('studio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['movie_library.Studio'])),
            ('release_date', self.gf('django.db.models.fields.DateField')()),
            ('headshot', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'movie_library', ['Movie'])

        # Adding M2M table for field writer on 'Movie'
        m2m_table_name = db.shorten_name(u'movie_library_movie_writer')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('movie', models.ForeignKey(orm[u'movie_library.movie'], null=False)),
            ('writer', models.ForeignKey(orm[u'movie_library.writer'], null=False))
        ))
        db.create_unique(m2m_table_name, ['movie_id', 'writer_id'])

        # Adding M2M table for field director on 'Movie'
        m2m_table_name = db.shorten_name(u'movie_library_movie_director')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('movie', models.ForeignKey(orm[u'movie_library.movie'], null=False)),
            ('director', models.ForeignKey(orm[u'movie_library.director'], null=False))
        ))
        db.create_unique(m2m_table_name, ['movie_id', 'director_id'])


    def backwards(self, orm):
        # Deleting model 'Studio'
        db.delete_table(u'movie_library_studio')

        # Deleting model 'Genre'
        db.delete_table(u'movie_library_genre')

        # Deleting model 'Writer'
        db.delete_table(u'movie_library_writer')

        # Deleting model 'Director'
        db.delete_table(u'movie_library_director')

        # Deleting model 'Movie'
        db.delete_table(u'movie_library_movie')

        # Removing M2M table for field writer on 'Movie'
        db.delete_table(db.shorten_name(u'movie_library_movie_writer'))

        # Removing M2M table for field director on 'Movie'
        db.delete_table(db.shorten_name(u'movie_library_movie_director'))


    models = {
        u'movie_library.director': {
            'Meta': {'object_name': 'Director'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'headshot': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'nick_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'salutation': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'movie_library.genre': {
            'Meta': {'object_name': 'Genre'},
            'explanation': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'movie_library.movie': {
            'Meta': {'object_name': 'Movie'},
            'director': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['movie_library.Director']", 'symmetrical': 'False'}),
            'headshot': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'release_date': ('django.db.models.fields.DateField', [], {}),
            'studio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['movie_library.Studio']"}),
            'synopsis': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'writer': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['movie_library.Writer']", 'symmetrical': 'False'})
        },
        u'movie_library.studio': {
            'Meta': {'object_name': 'Studio'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'state_province': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'movie_library.writer': {
            'Meta': {'object_name': 'Writer'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'headshot': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'salutation': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['movie_library']