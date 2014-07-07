from django.db import models

class QualCategory(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

class Qualification(models.Model):
    name = models.CharField(max_length=200, unique=True)
    image = models.ImageField(upload_to='qualifications/', blank=True)
    category = models.ForeignKey(QualCategory)

    def __str__(self):
        return self.name

class Personnel(models.Model):
    name = models.CharField(max_length=200, unique=True)
    image = models.ImageField(upload_to='qualifications', blank=True)

    def __str__(self):
        return self.name

class PersonnelQualification(models.Model):
    description = models.CharField(max_length=400, unique=True)
    person = models.ForeignKey(Personnel)

    def __str__(self):
        return self.description