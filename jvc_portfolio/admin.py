from django.contrib import admin

from .models import Project, Design, Development, Software, Program

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'name', 'project_type', 'designs', 'developments', 'image', 'created_on')
    list_filter = ('created_on',)
    search_fields = ('title', 'project_type')
    
    fields = ('title', 'name', 'image', 'about', 'sub_title', 'year', 'brief', 'fullpage_imgI', 'banner_textI', 'processI', 'fullpage_imgII', 'processII', 'fullpage_imgIII', 'fullpage_imgIV', 'processIII', 'processIV', 'fullpage_imgV', 'processV', 'fullpage_imgVI', 'processVI', 'processVII', 'fullpage_imgVII', 'processVIII', 'processIX', 'responsive_imgI', 'banner_textII', 'responsive_imgII', 'responsive_imgIII')

    def designs(self, obj):
        return obj.design_projects.all()

    def developments(self, obj):
        return obj.development_projects.all()

admin.site.register(Project, ProjectAdmin)

class DesignAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'project', 'created_on', 'brief', 'banner_img')
    list_filter = ('created_on',)
    search_fields = ('title', 'software')

admin.site.register(Design, DesignAdmin)

admin.site.register(Software)

class DevelopmentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'project', 'created_on', 'description', 'image')
    list_filter = ('created_on',)
    search_fields = ('title', 'programs')

admin.site.register(Development, DevelopmentAdmin)

class ProgramAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')

admin.site.register(Program, ProgramAdmin)
