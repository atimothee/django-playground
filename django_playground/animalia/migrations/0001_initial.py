# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Phylum'
        db.create_table(u'animalia_phylum', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'animalia', ['Phylum'])

        # Adding model 'Class'
        db.create_table(u'animalia_class', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('phylum', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['animalia.Phylum'])),
        ))
        db.send_create_signal(u'animalia', ['Class'])

        # Adding model 'Order'
        db.create_table(u'animalia_order', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('classe', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['animalia.Class'])),
        ))
        db.send_create_signal(u'animalia', ['Order'])

        # Adding model 'Family'
        db.create_table(u'animalia_family', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('order', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['animalia.Order'])),
        ))
        db.send_create_signal(u'animalia', ['Family'])

        # Adding model 'Genus'
        db.create_table(u'animalia_genus', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('family', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['animalia.Family'])),
        ))
        db.send_create_signal(u'animalia', ['Genus'])

        # Adding model 'Species'
        db.create_table(u'animalia_species', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('genus', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['animalia.Genus'])),
        ))
        db.send_create_signal(u'animalia', ['Species'])

        # Adding model 'Animal'
        db.create_table(u'animalia_animal', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('species', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['animalia.Species'])),
        ))
        db.send_create_signal(u'animalia', ['Animal'])


    def backwards(self, orm):
        # Deleting model 'Phylum'
        db.delete_table(u'animalia_phylum')

        # Deleting model 'Class'
        db.delete_table(u'animalia_class')

        # Deleting model 'Order'
        db.delete_table(u'animalia_order')

        # Deleting model 'Family'
        db.delete_table(u'animalia_family')

        # Deleting model 'Genus'
        db.delete_table(u'animalia_genus')

        # Deleting model 'Species'
        db.delete_table(u'animalia_species')

        # Deleting model 'Animal'
        db.delete_table(u'animalia_animal')


    models = {
        u'animalia.animal': {
            'Meta': {'object_name': 'Animal'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'species': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['animalia.Species']"})
        },
        u'animalia.class': {
            'Meta': {'object_name': 'Class'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'phylum': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['animalia.Phylum']"})
        },
        u'animalia.family': {
            'Meta': {'object_name': 'Family'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['animalia.Order']"})
        },
        u'animalia.genus': {
            'Meta': {'object_name': 'Genus'},
            'family': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['animalia.Family']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'animalia.order': {
            'Meta': {'object_name': 'Order'},
            'classe': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['animalia.Class']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'animalia.phylum': {
            'Meta': {'object_name': 'Phylum'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'animalia.species': {
            'Meta': {'object_name': 'Species'},
            'genus': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['animalia.Genus']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['animalia']