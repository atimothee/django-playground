# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Animal.admin_notes'
        db.add_column(u'animalia_animal', 'admin_notes',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Animal.admin_notes'
        db.delete_column(u'animalia_animal', 'admin_notes')


    models = {
        u'animalia.animal': {
            'Meta': {'object_name': 'Animal'},
            'admin_notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'species': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['animalia.Species']"}),
            'views': ('django.db.models.fields.IntegerField', [], {'default': '0'})
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