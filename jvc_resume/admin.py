from django.contrib import admin

from .models import About, SupplimentalEducation, TechnicalSkills, ProgrammingProjects, Employment

# Register your models here.

class AboutAdmin(admin.ModelAdmin):
    list_display = ('text', 'pk', 'created_on')
 
admin.site.register(About, AboutAdmin)

class SupplimentalEducationAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'type', 'created_on')
    list_filter = ('name', )
    search_fields = ('name', )

admin.site.register(SupplimentalEducation, SupplimentalEducationAdmin)

class TechnicalSkillsAdmin(admin.ModelAdmin):
    list_display = ('type', 'created_on')
    list_filter = ('type', 'programs')
    search_fileds = ('type', 'programs')

admin.site.register(TechnicalSkills, TechnicalSkillsAdmin)

class ProgrammingProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_on')
    list_filter = ('name', )
    search_fields = ('name', )

admin.site.register(ProgrammingProjects, ProgrammingProjectAdmin)

class EmploymentAdmin(admin.ModelAdmin):
    list_display = ('name', 'job_title', 'start_date', 'start_year', 'end_date', 'end_year', 'created_on')
    list_filter = ('name', 'job_title', 'start_date', 'end_date')
    search_fields = ('name', 'job_title')

admin.site.register(Employment, EmploymentAdmin)
