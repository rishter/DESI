from django.db import models

class QualCategory(models.Model):
    name = models.CharField(max_length=200)
    name_short = models.CharField("name to use in link (must have no spaces)", max_length=20, unique=True)

    def __str__(self):
        return self.name

class Qualification(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='qualifications/', blank=True)
    category = models.ForeignKey(QualCategory)

    def __str__(self):
        return self.name

