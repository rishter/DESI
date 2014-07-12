from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from django.template import RequestContext, loader
from projects.models import Project, ProjectCategory, ProjectImage
from django.views import generic

from utils.strings import strip_md

def index(request):
    project_categories = ProjectCategory.objects.all()
    projects = Project.objects.all()
    images = ProjectImage.objects.all()
    for project in projects:
        project.main_image = [image for image in images if image.project_id == project.id and image.is_main_image]
        project.plain_desc = strip_md(project.description)
    for category in project_categories:
        category.projects = [project for project in projects if project.category_id == category.id]
    return render(request, 'projects/index.html', { 'project_categories': project_categories })

def detail(request, proj_name_short):
    project = get_object_or_404(Project, name_short=proj_name_short)
    images = ProjectImage.objects.all()
    side_images = []
    normal_images = []
    for image in images:
        if image.project_id == project.id:
            if image.side_image:
                side_images.append(image)
            elif image.is_main_image:
                project.main_image = image
            else:
                normal_images.append(image)    

    return render(request, 'projects/detail.html', {'project': project, 'side_images': side_images, 'normal_images': normal_images,})


def categoryPrettyPrint(category):
    return category.name + ': ' + ', '.join([project.name_long for project in category.projects])
