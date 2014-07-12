from django.db import models

from clients.models import Client


class ServiceCategory(models.Model):
    name = models.CharField(max_length=200, unique=True)
    subheading = models.CharField(max_length=200, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.name

class ServiceImage(models.Model):
    image = models.ImageField(upload_to='service_images/')
    category = models.ForeignKey(ServiceCategory)

    def __str__(self):
        return "image in " + str(self.category)

class ProjectService(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(ServiceCategory)

    def __str__(self):
        return self.name

class ProjectCategory(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

class ProjectOwner(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.name

class ProjectLocation(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    category = models.ForeignKey(ProjectCategory)
    desi_id = models.CharField(max_length=200, unique=True)
    name_long = models.CharField(max_length=200)
    name_short = models.CharField("name to use as url", max_length=200, unique=True)
    description = models.TextField()
    services = models.ManyToManyField(ProjectService)
    project_owner = models.ForeignKey(ProjectOwner, blank=True, null=True)
    project_client = models.ForeignKey(Client, blank=True)
    owner_is_client = models.BooleanField()
    project_location = models.ForeignKey(ProjectLocation)
    use_in_carousel = models.BooleanField()

    def __str__(self):
        return self.name_long

class ProjectImage(models.Model):
    image = models.ImageField(upload_to='project_images/')
    side_image = models.BooleanField()
    project = models.ForeignKey(Project)
    is_main_image = models.BooleanField()
