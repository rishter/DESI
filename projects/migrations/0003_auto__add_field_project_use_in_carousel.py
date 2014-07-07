# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Project.use_in_carousel'
        db.add_column('projects_project', 'use_in_carousel',
                      self.gf('django.db.models.fields.BooleanField')(default=None),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Project.use_in_carousel'
        db.delete_column('projects_project', 'use_in_carousel')


    models = {
        'projects.client': {
            'Meta': {'object_name': 'Client'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'testimony': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        'projects.project': {
            'Meta': {'object_name': 'Project'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.ProjectCategory']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'desi_id': ('django.db.models.fields.CharField', [], {'max_length': '200', 'unique': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_long': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name_short': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'owner_is_client': ('django.db.models.fields.BooleanField', [], {}),
            'project_client': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.Client']", 'blank': 'True'}),
            'project_location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.ProjectLocation']"}),
            'project_owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.ProjectOwner']", 'blank': 'True'}),
            'services': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['projects.ProjectService']", 'symmetrical': 'False'}),
            'use_in_carousel': ('django.db.models.fields.BooleanField', [], {})
        },
        'projects.projectcategory': {
            'Meta': {'object_name': 'ProjectCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'projects.projectimage': {
            'Meta': {'object_name': 'ProjectImage'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.Project']"}),
            'side_image': ('django.db.models.fields.BooleanField', [], {})
        },
        'projects.projectlocation': {
            'Meta': {'object_name': 'ProjectLocation'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'projects.projectowner': {
            'Meta': {'object_name': 'ProjectOwner'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'projects.projectservice': {
            'Meta': {'object_name': 'ProjectService'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['projects']