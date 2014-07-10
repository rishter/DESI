from django.shortcuts import render

from projects.models import Project, ProjectImage, ProjectService, ServiceCategory
from news.models import Article

from markdown import markdown
from datetime import date

from utils.strings import strip_md

def index(request):
    carousel_projects = Project.objects.filter(use_in_carousel=True)
    main_images = ProjectImage.objects.filter(is_main_image=True)
    for project in carousel_projects:
        project.main_image = [image for image in main_images if image.project_id == project.id]

    carousel_range = range(len(carousel_projects))

    start_date = date(2014, 7, 1)
    now = date.today()
    news = Article.objects.order_by('date').reverse().filter(date__range=(start_date,now))[:3]
    for article in news:
    	article.text = strip_md(article.text)

    return render(request, 'all/index.html', {'carousel_projects': carousel_projects, 'carousel_range': carousel_range, 'news': news})

def services(request):
	categories = ServiceCategory.objects.all()
	services = ProjectService.objects.all()
	for category in categories:
		category.services = [service for service in services if service.category_id == category.id]

	return render(request, 'all/services.html', {})



def contact(request):
	return render(request, 'all/contact.html', {})

def about(request):
	return render(request, 'all/about.html', {})