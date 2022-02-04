from django.contrib import admin

from .models import Project, Design, Development, Software, Program

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'project_type', 'designs', 'created_on')
    list_filter = ('created_on',)
    search_fields = ('title', 'project_type')

    def designs(self, obj):
        return obj.design_projects.all()

admin.site.register(Project, ProjectAdmin)

class DesignAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'project', 'created_on', 'description')
    list_filter = ('created_on',)
    search_fields = ('title', 'software')

admin.site.register(Design, DesignAdmin)

admin.site.register(Software)

class DevelopmentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'project', 'created_on', 'description')
    list_filter = ('created_on',)
    search_fields = ('title', 'programs')

admin.site.register(Development, DevelopmentAdmin)

admin.site.register(Program)
