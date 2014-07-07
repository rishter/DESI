# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ProjectCategory'
        db.create_table('projects_projectcategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('projects', ['ProjectCategory'])

        # Adding model 'ProjectService'
        db.create_table('projects_projectservice', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('projects', ['ProjectService'])

        # Adding model 'ProjectOwner'
        db.create_table('projects_projectowner', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('address', self.gf('django.db.models.fields.CharField')(blank=True, max_length=200)),
        ))
        db.send_create_signal('projects', ['ProjectOwner'])

        # Adding model 'Client'
        db.create_table('projects_client', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('address', self.gf('django.db.models.fields.CharField')(blank=True, max_length=200)),
            ('logo', self.gf('django.db.models.fields.files.ImageField')(blank=True, max_length=100)),
            ('testimony', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('projects', ['Client'])

        # Adding model 'ProjectLocation'
        db.create_table('projects_projectlocation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('projects', ['ProjectLocation'])

        # Adding model 'Project'
        db.create_table('projects_project', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projects.ProjectCategory'])),
            ('desi_id', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
            ('name_long', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('name_short', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('location_short_string', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('project_owner', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, to=orm['projects.ProjectOwner'])),
            ('project_client', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, to=orm['projects.Client'])),
            ('owner_is_client', self.gf('django.db.models.fields.BooleanField')()),
            ('project_location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projects.ProjectLocation'])),
        ))
        db.send_create_signal('projects', ['Project'])

        # Adding M2M table for field services on 'Project'
        m2m_table_name = db.shorten_name('projects_project_services')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm['projects.project'], null=False)),
            ('projectservice', models.ForeignKey(orm['projects.projectservice'], null=False))
        ))
        db.create_unique(m2m_table_name, ['project_id', 'projectservice_id'])

        # Adding model 'ProjectImage'
        db.create_table('projects_projectimage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('side_image', self.gf('django.db.models.fields.BooleanField')()),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projects.Project'])),
        ))
        db.send_create_signal('projects', ['ProjectImage'])


    def backwards(self, orm):
        # Deleting model 'ProjectCategory'
        db.delete_table('projects_projectcategory')

        # Deleting model 'ProjectService'
        db.delete_table('projects_projectservice')

        # Deleting model 'ProjectOwner'
        db.delete_table('projects_projectowner')

        # Deleting model 'Client'
        db.delete_table('projects_client')

        # Deleting model 'ProjectLocation'
        db.delete_table('projects_projectlocation')

        # Deleting model 'Project'
        db.delete_table('projects_project')

        # Removing M2M table for field services on 'Project'
        db.delete_table(db.shorten_name('projects_project_services'))

        # Deleting model 'ProjectImage'
        db.delete_table('projects_projectimage')


    models = {
        'projects.client': {
            'Meta': {'object_name': 'Client'},
            'address': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '200'}),
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
            'location_short_string': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name_long': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name_short': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'owner_is_client': ('django.db.models.fields.BooleanField', [], {}),
            'project_client': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['projects.Client']"}),
            'project_location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.ProjectLocation']"}),
            'project_owner': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['projects.ProjectOwner']"}),
            'services': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['projects.ProjectService']"})
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
            'address': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '200'}),
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