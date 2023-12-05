from django.urls import path

from . import views

urlpatterns = [
    
    path('about/', views.AboutView.as_view(), name='about'),

    path('update_about/', views.UpdateAboutView.as_view(), name='add_about'),
    
    path('populate_form/', views.PopulateForm.as_view(), name='populate_form'),

    path('add_edu/', views.AddEduView.as_view(), name='add_edu'),
    path('update_edu/', views.UpdateEduView.as_view(), name='update_edu'),

    path('add_tech_skill/', views.AddTechSkillView.as_view(), name='add_techskill'),
    path('update_tech_skill/', views.UpdateTechSkill.as_view(), name='update_tech_skill'),

    path('add_programming_project/', views.AddProgrammingProjectView.as_view(), name='add_programming_project'),
    path('update_prog_proj/', views.UpdateProgrammingProject.as_view(), name='update_prog_proj'),

    path('add_employment/', views.AddEmploymentView.as_view(), name='add_employment'),
    path('update_employment/', views.UpdateEmployment.as_view(), name='update_employment'),
]