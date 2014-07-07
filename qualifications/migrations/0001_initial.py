# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'QualCategory'
        db.create_table('qualifications_qualcategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200, unique=True)),
        ))
        db.send_create_signal('qualifications', ['QualCategory'])

        # Adding model 'Qualification'
        db.create_table('qualifications_qualification', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200, unique=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['qualifications.QualCategory'])),
        ))
        db.send_create_signal('qualifications', ['Qualification'])

        # Adding model 'Personnel'
        db.create_table('qualifications_personnel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200, unique=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
        ))
        db.send_create_signal('qualifications', ['Personnel'])

        # Adding model 'PersonnelQualification'
        db.create_table('qualifications_personnelqualification', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=400, unique=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['qualifications.Personnel'])),
        ))
        db.send_create_signal('qualifications', ['PersonnelQualification'])


    def backwards(self, orm):
        # Deleting model 'QualCategory'
        db.delete_table('qualifications_qualcategory')

        # Deleting model 'Qualification'
        db.delete_table('qualifications_qualification')

        # Deleting model 'Personnel'
        db.delete_table('qualifications_personnel')

        # Deleting model 'PersonnelQualification'
        db.delete_table('qualifications_personnelqualification')


    models = {
        'qualifications.personnel': {
            'Meta': {'object_name': 'Personnel'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'unique': 'True'})
        },
        'qualifications.personnelqualification': {
            'Meta': {'object_name': 'PersonnelQualification'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '400', 'unique': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['qualifications.Personnel']"})
        },
        'qualifications.qualcategory': {
            'Meta': {'object_name': 'QualCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'unique': 'True'})
        },
        'qualifications.qualification': {
            'Meta': {'object_name': 'Qualification'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['qualifications.QualCategory']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'unique': 'True'})
        }
    }

    complete_apps = ['qualifications']