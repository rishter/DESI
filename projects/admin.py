from django.contrib import admin

from projects.models import Project, ProjectService, ProjectCategory, ProjectOwner, ProjectImage, ProjectLocation, ServiceCategory

class ImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 2


class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Project Info',    {'fields': ['desi_id', 'name_long', 'name_short', 'project_location', 'description']}),
        ('Connection to DESI', {'fields': ['category', 'services', 'project_owner', 'project_client', 'owner_is_client', 'use_in_carousel']}),
    ]
    inlines = [ImageInline]
    list_display = ('desi_id', 'name_long', 'project_location')
    search_fields = ['desi_id', 'name_long']
    list_filter = ['project_location']

class ServiceAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}

class ServiceCategoryAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}

class CategoryAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}

class LocationAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}

class OwnerAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}



admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectService, ServiceAdmin)
admin.site.register(ServiceCategory, ServiceCategoryAdmin)
admin.site.register(ProjectCategory)
admin.site.register(ProjectLocation, LocationAdmin)
admin.site.register(ProjectOwner, OwnerAdmin)
