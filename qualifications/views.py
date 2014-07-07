from django.shortcuts import render

from qualifications.models import QualCategory, Qualification, Personnel, PersonnelQualification

def index(request):
    qual_categories = QualCategory.objects.all()
    quals = Qualification.objects.all()
    pers = Personnel.objects.all()
    persquals = PersonnelQualification.objects.all()
    for category in qual_categories:
        category.quals = [qual for qual in quals if qual.category_id == category.id]
    for per in pers:
        per.qualifications = [persqual for persqual in persquals if persqual.person_id == per.id]

    return render(request, 'qualifications/index.html', { 'qualification_categories': qual_categories, 'personnel': pers })