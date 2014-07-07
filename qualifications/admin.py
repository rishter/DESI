from django.contrib import admin

from qualifications.models import Qualification, QualCategory, Personnel, PersonnelQualification

class PersonnelInline(admin.TabularInline):
    model = PersonnelQualification
    extra = 3

class PersonnelAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Personnel Info', {'fields': ['name', 'image']})
    ]
    inlines = [PersonnelInline]
    search_fields = ['name']

class QualificationAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Qualification Information', {'fields': ['name', 'image', 'category']})
    ]
    search_fields = ['name']

class CategoryAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}

admin.site.register(Personnel, PersonnelAdmin)
admin.site.register(Qualification, QualificationAdmin)
admin.site.register(QualCategory, CategoryAdmin)