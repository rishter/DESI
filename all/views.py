from django.shortcuts import render

from projects.models import Project, ProjectImage

def index(request):
    projects = Project.objects.all()
    images = ProjectImage.objects.all()
    carousel_projects = [project for project in projects if project.use_in_carousel]
    for project in carousel_projects:
        project.main_image = [image for image in images if image.project_id == project.id and image.is_main_image]

    return render(request, 'all/index.html', {'carousel_projects': carousel_projects})