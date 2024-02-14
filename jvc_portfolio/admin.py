from django.contrib import admin

from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import Project, Design, Development, Software, Program

# Register your models here.

class CustomUserAdim(BaseUserAdmin):
    
    list_display = ('pk', 'username', 'email', 'is_staff')

admin.site.unregister(User)    
admin.site.register(User, CustomUserAdim)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'name', 'project_type', 'designs', 'developments', 'image', 'created_on')
    list_filter = ('created_on',)
    search_fields = ('title', 'project_type')
    
    fields = ('title', 'name', 'link', 'image', 'about', 'sub_title', 'description', 'year', 'brief', 'fullpage_imgI', 'banner_textI', 'processI', 'fullpage_imgII', 'processII', 'fullpage_imgIII', 'fullpage_imgIV', 'processIII', 'processIV', 'fullpage_imgV', 'processV', 'fullpage_imgVI', 'processVI', 'processVII', 'fullpage_imgVII', 'processVIII', 'processIX', 'responsive_imgI', 'banner_textII', 'responsive_imgII', 'responsive_imgIII')

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
