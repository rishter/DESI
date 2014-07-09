from django.contrib import admin

from qualifications.models import Qualification, QualCategory

class QualificationAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Qualification Information', {'fields': ['name', 'image', 'category']})
    ]
    search_fields = ['name']
    list_display = ('name', 'category')
    list_filter = ['category']

class CategoryAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}

admin.site.register(Qualification, QualificationAdmin)
admin.site.register(QualCategory)