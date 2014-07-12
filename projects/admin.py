from django.contrib import admin

from projects.models import Project, ProjectService, ProjectCategory, ProjectOwner, ProjectImage, ProjectLocation, ServiceCategory, ServiceImage

class ImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 2

class ServiceImageInline(admin.TabularInline):
    model = ServiceImage
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

class ServiceCategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Information', {'fields': ['name', 'subheading', 'description']})
    ]
    inlines = [ServiceImageInline]
    list_display = ('name', 'subheading')
    search_fields = ['name', 'subheading', 'description']

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    list_filter = ['category']

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
