# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'ProjectOwner.address_text'
        db.delete_column('projects_projectowner', 'address_text')

        # Adding field 'ProjectOwner.address'
        db.add_column('projects_projectowner', 'address',
                      self.gf('django.db.models.fields.TextField')(blank=True, default=''),
                      keep_default=False)

        # Deleting field 'Client.address_text'
        db.delete_column('projects_client', 'address_text')

        # Adding field 'Client.address'
        db.add_column('projects_client', 'address',
                      self.gf('django.db.models.fields.TextField')(blank=True, default=''),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'ProjectOwner.address_text'
        db.add_column('projects_projectowner', 'address_text',
                      self.gf('django.db.models.fields.TextField')(blank=True, default=''),
                      keep_default=False)

        # Deleting field 'ProjectOwner.address'
        db.delete_column('projects_projectowner', 'address')

        # Adding field 'Client.address_text'
        db.add_column('projects_client', 'address_text',
                      self.gf('django.db.models.fields.TextField')(blank=True, default=''),
                      keep_default=False)

        # Deleting field 'Client.address'
        db.delete_column('projects_client', 'address')


    models = {
        'projects.client': {
            'Meta': {'object_name': 'Client'},
            'address': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'blank': 'True', 'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'testimony': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        'projects.project': {
            'Meta': {'object_name': 'Project'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.ProjectCategory']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'desi_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_long': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name_short': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'owner_is_client': ('django.db.models.fields.BooleanField', [], {}),
            'project_client': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['projects.Client']"}),
            'project_location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.ProjectLocation']"}),
            'project_owner': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['projects.ProjectOwner']"}),
            'services': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['projects.ProjectService']"}),
            'use_in_carousel': ('django.db.models.fields.BooleanField', [], {})
        },
        'projects.projectcategory': {
            'Meta': {'object_name': 'ProjectCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'})
        },
        'projects.projectimage': {
            'Meta': {'object_name': 'ProjectImage'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'is_main_image': ('django.db.models.fields.BooleanField', [], {}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.Project']"}),
            'side_image': ('django.db.models.fields.BooleanField', [], {})
        },
        'projects.projectlocation': {
            'Meta': {'object_name': 'ProjectLocation'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'})
        },
        'projects.projectowner': {
            'Meta': {'object_name': 'ProjectOwner'},
            'address': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'projects.projectservice': {
            'Meta': {'object_name': 'ProjectService'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.ServiceCategory']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'projects.servicecategory': {
            'Meta': {'object_name': 'ServiceCategory'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'repr_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['projects']