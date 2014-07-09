from django.shortcuts import render

from qualifications.models import QualCategory, Qualification

def index(request):
    qual_categories = QualCategory.objects.all()
    quals = Qualification.objects.order_by('name')
    for category in qual_categories:
        category.quals = [qual for qual in quals if qual.category_id == category.id]

    return render(request, 'qualifications/index.html', { 'qualification_categories': qual_categories, })